import Post from "../post/Post";
import Share from "../share/Share";
import "./feed.css";
import { Posts } from "../../dummyData";
import { useEffect, useRef, useState } from "react";
import axios from "axios"
axios.defaults.withCredentials = true;



const Feed = ({user_id}) => {

  const PF = import.meta.env.VITE_API_URL
  
  const [posts, setPosts] = useState([]);
  const [nextData, setNextData] = useState(user_id ? PF+"/post/user_posts/"+user_id+"/" : PF+"/post/user_posts/");
  const [isLoading, setIsLoading] = useState(false);
  


  const fetchPosts = async () => {
    setIsLoading(true);
    try{
      const res = await axios.get(nextData);
      const data = await res.data
      if(data.results){
        setPosts(prevItems => [...prevItems, ...data.results]);
      }
      setNextData( prev_url => (data.next && prev_url !== data.next) ? data.next : null);
      
    }
    catch(err){}
    finally{
      setIsLoading(false);
    }
  };

  const handelInfiniteScroll = async () => {
    try {
      if (window.innerHeight + document.documentElement.scrollTop + 0.3 >= document.documentElement.scrollHeight) 
      {
        if(nextData){
          fetchPosts();
        }
        else{ return }
      }

    } catch (error) {
      console.log(error);
    }
  };

  useEffect(() => {
    window.addEventListener("scroll", handelInfiniteScroll);
    return () => window.removeEventListener("scroll", handelInfiniteScroll);
  }, [isLoading]);


  return (
    <div className="feed">
      <div className="feedWrapper">
        <Share />
        { posts ? posts.map((p) => (
          <Post key={p.id} post={p} />
        )): <p>Loading...</p>}
      </div>
    </div>
  );
};


export default Feed;