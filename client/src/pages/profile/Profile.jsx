import "./profile.css";
import Topbar from "../../components/topbar/Topbar";
import Sidebar from "../../components/sidebar/Sidebar";
import Feed from "../../components/feed/Feed";
import Rightbar from "../../components/rightbar/Rightbar";
import { getImageUrl } from "../../utils";
import { memo, useCallback, useEffect, useRef, useState } from "react";
import { useParams } from "react-router-dom";
import axios from "axios";
axios.defaults.withCredentials = true;



const Profile = () => {

  const [user, setUser] = useState({});
  const userId = useParams().user_id

  const rn = useRef(0);

  rn.current = rn.current + 1;
  console.log(rn.current);

  useEffect(() => {
    const fetchUser = async () => {
      const res = await axios.get(import.meta.env.VITE_API_URL + "/user/profile/"+userId+"/")
      if(JSON.stringify(res.data) !== JSON.stringify(user)){
        setUser(res.data)
      }
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
                <h4 className="profileInfoName">{user.user ? user.user.username : ""}</h4>
                <span className="profileInfoDesc">{user.user ? user.bio : ""}</span>
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
};

export default memo(Profile);