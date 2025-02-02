import { useContext, useState } from "react";
import "./Popup.css"
import axios from "axios";
import { AuthContext } from "../../context/AuthContext";

const UploadImage = ({togglePoupup, setUser, userId}) => {
    const PF = import.meta.env.VITE_API_URL;

    const getCSRFToken = () => {
        const csrfToken = document.cookie
          .split('; ')
          .find(row => row.startsWith('csrftoken='));  // Replace 'csrf_token' with your actual cookie name
        return csrfToken ? csrfToken.split('=')[1] : null;
      };
    

    const handleImageUpload = async (e) => {
        const file = e.target.files[0];
        if(file){
            const data = new FormData();
            data.append("profile_img", file);
            const res = await axios.put(PF+"/user/profile/"+userId+"/", data,{ headers : {"X-CSRFToken" : getCSRFToken()} });
            const res_data = await res.data
            console.log(res_data);
            setUser(res_data)
            const storedUser = JSON.parse(localStorage.getItem('user'));
            console.log(storedUser["payload"]);
            const parsedUrl = new URL(res_data.profile_img);
            storedUser.payload.profile_img = parsedUrl.pathname
            localStorage.setItem('user', JSON.stringify(storedUser));

            // setUserContext(prev => ({...prev, }))
            
        }
        togglePoupup(prev => !prev);
    }

    return (
        <div className="popup">
            <div className="innerBox">
                <h2>Change Profile Photo</h2>
                <hr />
                <label htmlFor="profilePic">
                    <span>Upload Photo</span>
                    <input type="file" id="profilePic" accept=".png, .jpeg, .jpg" onChange={handleImageUpload} />   
                </label>
                <hr/>
                <button className="removeImg">Delete Current Photo</button>
                <hr />
                <button onClick={()=> togglePoupup(prev => !prev)}>Cancel</button>
            </div>
        </div>
    )
}


export default UploadImage;