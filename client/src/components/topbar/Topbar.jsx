import "./topbar.css";
import ChatIcon from '@mui/icons-material/Chat';
import SearchIcon from "@mui/icons-material/Search"
import PersonIcon from "@mui/icons-material/Person"
import NotificationsIcon from "@mui/icons-material/Notifications"
import { getImageUrl } from "../../utils";
import { Link } from "react-router-dom";
import { AuthContext } from "../../context/AuthContext";
import { memo, useContext, useEffect, useRef, useState } from "react";
import LogoutIcon from '@mui/icons-material/Logout';
import axios from "axios";

axios.defaults.withCredentials = true;




const getCSRFToken = () => {
  const csrfToken = document.cookie
    .split('; ')
    .find(row => row.startsWith('csrftoken='));  // Replace 'csrf_token' with your actual cookie name
  return csrfToken ? csrfToken.split('=')[1] : null;
};


const logoutUser = async () => {
  const pf = import.meta.env.VITE_API_URL
  try{
    await axios.post(pf+"/auth/logout/",{data: null}, { headers : {"X-CSRFToken" : getCSRFToken()}});
    sessionStorage.clear();
    localStorage.clear();
    document.cookie = `sessionid=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/`;
    window.location.href = '/login/'
  }
  catch{}
}


const NotifyDispaly = ({array}) => {
  return (
    <div className="notifycontainer">
      {array && array.map((itm) => (
        <p>{itm.message}</p>
      ))}
    </div>
  )
}


const  Topbar = memo(() => {
  const { user } =  useContext(AuthContext);
  const rno = useRef(0);
  const [notificationCnt, setNotificationCnt] = useState(0)
  const [notificationList, setNotificationList] = useState([]);
  const notifications = async () => {
    const pf = import.meta.env.VITE_API_URL+"/notifications/"+user.payload.id+"/"
    try{
      const res = await axios.get(pf);
      setNotificationCnt(res.data.count);
      setNotificationList((prev) => [...prev, ...res.data.results]);
    }
    catch{}
  }

  useEffect(()=>{
    notifications();
  },[])


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
            {/* <span className="topbarIconBadge"></span> */}
          </div>
          <div className="topbarIconItem">
            <ChatIcon />
            {/* <span className="topbarIconBadge"></span> */}
          </div>
          <div className="topbarIconItem">
            <NotificationsIcon />
            <span className="topbarIconBadge">{ notificationCnt }</span>
            <NotifyDispaly array={notificationList}/>
          </div>
        </div>
        
        {/* <img src={getImageUrl("person/1.jpeg")} alt="" className="topbarImg"/> */}

        <div className="profilelogoutwrapper">
          <button onClick={logoutUser} className="logoutBtn"><span title="logout"><LogoutIcon/></span></button>
          <Link to={`/profile/${user.payload.id}`}>
            <img src={import.meta.env.VITE_API_URL + user.payload.profile_img} alt="" className="topbarImg"/>
          </Link>
        </div>
      </div>
    </div>
  );
});

export default Topbar;