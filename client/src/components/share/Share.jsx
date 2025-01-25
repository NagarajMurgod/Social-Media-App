import "./share.css";
import PermMediaIcon from '@mui/icons-material/PermMedia';
import LabelIcon from '@mui/icons-material/Label';
import RoomIcon from '@mui/icons-material/Room';
import EmojiEmotionsIcon from '@mui/icons-material/EmojiEmotions';
import { getImageUrl } from "../../utils";
import { useContext, useRef, useState } from "react";
import { AuthContext } from "../../context/AuthContext";
import axios from "axios";
// import { AuthContext } from "../../context/AuthContext";

export default function Share() {
  
  const {user}= useContext(AuthContext);
  const [file, setFile] = useState(null);
  const desc = useRef();
  const PF = import.meta.env.VITE_API_URL;


  const getCSRFToken = () => {
    const csrfToken = document.cookie
      .split('; ')
      .find(row => row.startsWith('csrftoken='));  // Replace 'csrf_token' with your actual cookie name
    return csrfToken ? csrfToken.split('=')[1] : null;
  };

  const submitHandler = async (e) => {
    e.preventDefault();
    const newPost = {
      "caption" : desc.current.value
    }

    if(file){
      const data = new FormData();
      const fileName = Date.now() + file.name;
      data.append("name", fileName);
      data.append("image", file);
      data.append("caption", desc.current.value)
      newPost.image = fileName;
      
      try{
        await axios.post(PF+"/post/upload/",{data: null}, { headers : {"X-CSRFToken" : getCSRFToken()} });
      }
      catch(err){
        console.log(err);
      }
      
    }
  }

  return (
    <div className="share">
      <div className="shareWrapper">
        <div className="shareTop">
          <img className="shareProfileImg" src={PF + user.payload.profile_img} alt="" />
          <input
            placeholder="What's in your mind Safak?"
            className="shareInput"
            ref = {desc}
          />
        </div>
        <hr className="shareHr"/>
        <form className="shareBottom" onSubmit={submitHandler}>
            <div className="shareOptions">
                <label htmlFor="file" className="shareOption">
                    <PermMediaIcon htmlColor="tomato" className="shareIcon"/>
                    <span className="shareOptionText">Photo or Video</span>
                    <input style={{display:"none"}} type="file" id="file" accept=".png, .jpeg, .jpg" onChange={(e)=>setFile(e.target.files[0])} />
                </label>
                <div className="shareOption">
                    <LabelIcon htmlColor="blue" className="shareIcon"/>
                    <span className="shareOptionText">Tag</span>
                </div>
                <div className="shareOption">
                    <RoomIcon htmlColor="green" className="shareIcon"/>
                    <span className="shareOptionText">Location</span>
                </div>
                <div className="shareOption">
                    <EmojiEmotionsIcon htmlColor="goldenrod" className="shareIcon"/>
                    <span className="shareOptionText">Feelings</span>
                </div>
            </div>
            <button type="submit" className="shareButton">Share</button>
        </form>
      </div>
    </div>
  );
}
