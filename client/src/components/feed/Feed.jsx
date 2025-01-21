import Post from "../post/Post";
import Share from "../share/Share";
import "./feed.css";
import { Posts } from "../../dummyData";
import { useEffect, useState } from "react";
import axios from "axios"

axios.defaults.withCredentials = true;


export default function Feed() {
  
  const [posts, setPosts] = useState([]);

  useEffect(()=>{
    const fetchPosts = async () => {
      const res = await axios.get(import.meta.env.VITE_API_URL + "/post/user_posts/");
      const data = res.data
      console.log(data)
      setPosts(data)
    };
    fetchPosts();
  },[]);
  

  return (
    <div className="feed">
      <div className="feedWrapper">
        <Share />
        
        { posts.results ? posts.results.map((p) => (
          <Post key={p.id} post={p} />
        )): <p>Loading...</p>}
      </div>
    </div>
  );
}
