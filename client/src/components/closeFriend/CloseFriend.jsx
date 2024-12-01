import "./closeFriend.css";
import { getImageUrl } from "../../utils";

export default function CloseFriend({user}) {
  return (
    <li className="sidebarFriend">
      <img className="sidebarFriendImg" src={getImageUrl(user.profilePicture)} alt="" />
      <span className="sidebarFriendName">{user.username}</span>
    </li>
  );
}
