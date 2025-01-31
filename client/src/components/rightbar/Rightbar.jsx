import "./rightbar.css";
import { Users } from "../../dummyData";
import Online from "../online/Online";
import { getImageUrl } from "../../utils";
import { useEffect, useRef, useState } from "react";
import axios from "axios";


axios.defaults.withCredentials = true;


const Rightbar = ({ user, user_id }) => {

  const [follow, setFollow] = useState(true)
  const [followers, setFollowers] = useState([])
  const PF = import.meta.env.VITE_API_URL

  const HomeRightbar = () => {
    return (
      <>
        <div className="birthdayContainer">
          <img className="birthdayImg" src={getImageUrl("gift.png")} alt="" />
          <span className="birthdayText">
            <b>Pola Foster</b> and <b>3 other friends</b> have a birhday today.
          </span>
        </div>
        <img className="rightbarAd" src={getImageUrl("ad.png")} alt="" />
        <h4 className="rightbarTitle">Online Friends</h4>
        <ul className="rightbarFriendList">
          {Users.map((u) => (
            <Online key={u.id} user={u} />
          ))}
        </ul>
      </>
    );
  };


  const getUsers = async (rel) => {
   
    const res = await axios.get(PF+`/user/profile/${user_id}/relations/?type=${rel}`)
    // console.log(res.data);
    const data = await res.data
    setFollowers(data);

  }

  useEffect(()=>{
    getUsers("followers");
  },[])

  const getFollowers = async (rel) => {
    setFollow(prev => !prev);
    getUsers(rel)
  }
  
  const ProfileRightbar = () => {

    return (
      <>
        <h4 className="rightbarTitle">User information</h4>
        <div className="rightbarInfo">
          <div className="rightbarInfoItem">
            <span className="rightbarInfoKey">First Name: </span>
            <span className="rightbarInfoValue">{user.user.first_name }</span>
          </div>
          <div className="rightbarInfoItem">
            <span className="rightbarInfoKey">Last Name:</span>
            <span className="rightbarInfoValue">{ user.user.last_name}</span>
          </div>
          <div className="rightbarInfoItem">
            <span className="rightbarInfoKey">Followers:</span>
            <span className="rightbarInfoValue">{user.followers}</span>
          </div>
          <div className="rightbarInfoItem">
            <span className="rightbarInfoKey">Following:</span>
            <span className="rightbarInfoValue">{user.following}</span>
          </div>
        </div>
        <div className="rightbarTitle">
          <button disabled = {follow} 
                  onClick={() => getFollowers("followers")} 
                  style={{borderBottom: follow ? "1px solid black" : "0px"}}>
                  Followers
            </button>

          <button disabled = {!follow} 
                  onClick={() => getFollowers("following")} 
                  style={{borderBottom: !follow ? "1px solid black" : "0px"}} >
                  Following
          </button>
          
        </div>
        <div className="rightbarFollowings"> 
          {followers.map((friend) => (
            <div key={friend.id} className="rightbarFollowing">
              <img
                // src={getImageUrl("person/1.jpeg")}
                src={friend.profile_img}
                alt=""
                className="rightbarFollowingImg"
              />
            <span className="rightbarFollowingName">{friend.username}</span>
          </div>
          ))}

        </div>
      </>
    );
  };
  return (
    <div className="rightbar">
      <div className="rightbarWrapper">
        {user ? <ProfileRightbar /> : <HomeRightbar />}
      </div>
    </div>
  );
};


export default Rightbar;