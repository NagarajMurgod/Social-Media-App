import "./closeFriend.css";
import { getImageUrl } from "../../utils";
import { Link } from "react-router-dom";

export default function CloseFriend({user}) {
  return (
    <a className="closeFriends" href={`/profile/${user.id}`}>
      <li className="sidebarFriend">
        <img className="sidebarFriendImg" src={user.profile_img} alt="" />
        <span className="sidebarFriendName">{user.username}</span>
      </li>
    </a>
  );
}
