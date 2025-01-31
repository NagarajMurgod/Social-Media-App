import "./sidebar.css";
import ChatIcon from '@mui/icons-material/Chat';
import PlayCircleFilledOutlinedIcon from "@mui/icons-material/PlayCircleFilledOutlined"
import GroupIcon from "@mui/icons-material/Group"
import RssFeedIcon from "@mui/icons-material/RssFeed"
import BookmarkIcon from "@mui/icons-material/Bookmark"
import HelpOutlineIcon from "@mui/icons-material/HelpOutline"
import WorkOutlineIcon from "@mui/icons-material/WorkOutline"
import EventIcon from "@mui/icons-material/Event"
import SchoolIcon from "@mui/icons-material/School"

import { Users } from "../../dummyData";
import CloseFriend from "../closeFriend/CloseFriend";
import { useEffect, useState } from "react";
import axios from "axios";

export default function Sidebar() {
  const PF = import.meta.env.VITE_API_URL
  const [userList, setUserList] = useState([])

  const getUserList = async (url) => {
    const res = await axios.get(url)
    const data = await res.data
    setUserList(data);
  }

  useEffect(()=>{
    getUserList(PF+"/user/list/")
  },[])

  return (
    <div className="sidebar">
      <div className="sidebarWrapper">
        <ul className="sidebarList">
          <li className="sidebarListItem">
            <RssFeedIcon className="sidebarIcon" />
            <span className="sidebarListItemText">Feed</span>
          </li>
          <li className="sidebarListItem">
            <ChatIcon className="sidebarIcon" />
            <span className="sidebarListItemText">Chats</span>
          </li>
          <li className="sidebarListItem">
            <PlayCircleFilledOutlinedIcon className="sidebarIcon" />
            <span className="sidebarListItemText">Videos</span>
          </li>
          <li className="sidebarListItem">
            <GroupIcon className="sidebarIcon" />
            <span className="sidebarListItemText">Groups</span>
          </li>
          <li className="sidebarListItem">
            <BookmarkIcon className="sidebarIcon" />
            <span className="sidebarListItemText">Bookmarks</span>
          </li>
          <li className="sidebarListItem">
            <HelpOutlineIcon className="sidebarIcon" />
            <span className="sidebarListItemText">Questions</span>
          </li>
          <li className="sidebarListItem">
            <WorkOutlineIcon className="sidebarIcon" />
            <span className="sidebarListItemText">Jobs</span>
          </li>
          <li className="sidebarListItem">
            <EventIcon className="sidebarIcon" />
            <span className="sidebarListItemText">Events</span>
          </li>
          <li className="sidebarListItem">
            <SchoolIcon className="sidebarIcon" />
            <span className="sidebarListItemText">Courses</span>
          </li>
        </ul>
        <button className="sidebarButton">Show More</button>
        <hr className="sidebarHr" />
        <ul className="sidebarFriendList">
          {userList.map((u) => (
            <CloseFriend key={u.id} user={u} />
          ))}
        </ul>
      </div>
    </div>
  );
}
