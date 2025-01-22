import "./topbar.css";
import ChatIcon from '@mui/icons-material/Chat';
import SearchIcon from "@mui/icons-material/Search"
import PersonIcon from "@mui/icons-material/Person"
import NotificationsIcon from "@mui/icons-material/Notifications"
import { getImageUrl } from "../../utils";
import { Link } from "react-router-dom";
import { AuthContext } from "../../context/AuthContext";
import { memo, useContext, useRef } from "react";


const  Topbar = memo(() => {
  const { user } =  useContext(AuthContext);
  const rno = useRef(0);

  return (
    <div className="topbarContainer">
      <div className="topbarLeft">
        <Link to="/" style={{textDecoration:"none"}}>
          <span className="logo">Lamasocial</span>
        </Link>
      </div>
      <div className="topbarCenter">
        <div className="searchbar">
          <SearchIcon className="searchIcon" />
          <input
            placeholder="SearchIcon for friend, post or video"
            className="searchInput"
          />
        </div>
      </div>
      <div className="topbarRight">
        <div className="topbarLinks">
          <span className="topbarLink">Homepage</span>
          <span className="topbarLink">Timeline</span>
        </div>
        <div className="topbarIcons">
          <div className="topbarIconItem">
            <PersonIcon />
            <span className="topbarIconBadge">1</span>
          </div>
          <div className="topbarIconItem">
            <ChatIcon />
            <span className="topbarIconBadge">2</span>
          </div>
          <div className="topbarIconItem">
            <NotificationsIcon />
            <span className="topbarIconBadge">1</span>
          </div>
        </div>
        {/* <img src={getImageUrl("person/1.jpeg")} alt="" className="topbarImg"/> */}
        <Link to={`/profile/${user.payload.id}`}>
          <img src={user ? import.meta.env.VITE_API_URL + user.payload.profile_img: getImageUrl("person/1.jpeg") } alt="" className="topbarImg"/>
        </Link>
      </div>
    </div>
  );
});

export default Topbar;