import "./profile.css";
import Topbar from "../../components/topbar/Topbar";
import Sidebar from "../../components/sidebar/Sidebar";
import Feed from "../../components/feed/Feed";
import Rightbar from "../../components/rightbar/Rightbar";
import UploadImage from "../../components/UploadProfilePopup/Popup";
import { getImageUrl } from "../../utils";
import { memo,useContext,useEffect, useRef, useState } from "react";
import { useParams } from "react-router-dom";
import axios from "axios";
import { AuthContext } from "../../context/AuthContext";

axios.defaults.withCredentials = true;



const Profile = () => {

  const [user, setUser] = useState({});
  const userId = useParams().user_id
  const [profilePopup, setProfilePopup] = useState(false);
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


  const handlePopUp = () => {
    setProfilePopup(prev => !prev)
  }

  return (
    <div className="profile_wrapper">
      <Topbar/>
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
                onClick={handlePopUp}
                className="profileUserImg"
                src={user.profile_img}
                alt=""
                style={{cursor:"pointer"}}
              />
              {profilePopup && <UploadImage togglePoupup={setProfilePopup} setUser={setUser} userId={userId}/>}
            </div>
            <div className="profileInfo">
                <h4 className="profileInfoName">{user.user ? user.user.username : ""}</h4>
                <span className="profileInfoDesc">{user.user ? user.bio : ""}</span>
            </div>
          </div>
          <div className="profileRightBottom">
            <Feed user_id={userId} profile_img = {user.profile_img ? user.profile_img : "..."} />
            { user.user ? <Rightbar user1 = {user} user_id={userId}/> : "loading.." }
          </div>
        </div>
      </div>
    </div>
  );
};

export default memo(Profile);