import "./profile.css";
import Topbar from "../../components/topbar/Topbar";
import Sidebar from "../../components/sidebar/Sidebar";
import Feed from "../../components/feed/Feed";
import Rightbar from "../../components/rightbar/Rightbar";
import { getImageUrl } from "../../utils";
import { useCallback, useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import axios from "axios";
axios.defaults.withCredentials = true;



export default function Profile() {

  const [user, setUser] = useState({});
  const userId = useParams().user_id

  useEffect(() => {
    const fetchUser = async () => {
      const res = await axios.get(import.meta.env.VITE_API_URL + "/user/profile/"+userId+"/")
      
      setUser(res.data)
    }
    fetchUser()
  },[]);

  return (
    <>
      <Topbar />
      <div className="profile">
        <Sidebar />
        <div className="profileRight">
          <div className="profileRightTop">
            <div className="profileCover">
              <img
                className="profileCoverImg"
                src={getImageUrl("post/3.jpeg")}
                alt=""
              />
              <img
                className="profileUserImg"
                src={user ? user.profile_img : getImageUrl("post/7.jpeg")}
                alt=""
              />
            </div>
            <div className="profileInfo">
                <h4 className="profileInfoName">{user.user ? user.user.username: ""}</h4>
                <span className="profileInfoDesc">{user ? user.bio : ""}</span>
            </div>
          </div>
          <div className="profileRightBottom">
            <Feed user_id={userId} />
            { user.user ? <Rightbar user = {user}/> : "loading.." }
          </div>
        </div>
      </div>
    </>
  );
}
