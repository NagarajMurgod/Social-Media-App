import Post from "../post/Post";
import Share from "../share/Share";
import "./feed.css";
import { Posts } from "../../dummyData";
import { useEffect, useRef, useState } from "react";
import axios from "axios"
import { useContext } from "react";
import { AuthContext } from "../../context/AuthContext";

axios.defaults.withCredentials = true;



const Feed = ({user_id}) => {

  const PF = import.meta.env.VITE_API_URL
  
  const [posts, setPosts] = useState([]);
  const [nextData, setNextData] = useState(user_id ? PF+"/post/user_posts/"+user_id+"/" : PF+"/post/user_posts/");
  const [loading, setLoading] = useState(false);
  const loadingRef = useRef(null);
  const user = useContext(AuthContext)

  const fetchPosts = async () => {
    if (loading) return; 
    setLoading(true);
    try{
      const res = await axios.get(nextData);
      const data = await res.data
      if(data.results){
        setPosts(prevItems => [...prevItems, ...data.results]);
      }
      setNextData(data.next ? data.next : null);
    }
    catch(err){}
    finally{
      setLoading(false);
    }
  };


  useEffect(() => {
    const observer = new IntersectionObserver(
      (entries) => {

        if (entries[0].isIntersecting) {
          fetchPosts()
        }
      },
      {
        threshold: 1
      }
    );

    if (loadingRef.current) {
      observer.observe(loadingRef.current);
    }
    return () => {
      if (loadingRef.current) {
        observer.unobserve(loadingRef.current);
      }
    };
  }, [loading, nextData]);

  return (
    <div className="feed">
      <div className="feedWrapper">
        
        {((user.user.payload.id == user_id) || !user_id) ? <Share /> : ""}

        {posts.map((p) => (
          <Post key={p.id} post={p} />
        ))}
        {nextData ? <p ref={loadingRef}>Loading...</p>:""}
    
      </div>
    </div>
  );
};


export default Feed;