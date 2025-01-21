import { useRef, useState } from "react";
import "./register.css";
import axios from "axios";
import { useNavigate } from "react-router-dom"

export default function Register() {

  const email = useRef();
  const password = useRef();
  const passwordAgain = useRef();
  const username = useRef();
  const [field_error, setFieldError] = useState("");
  const navigate =  useNavigate()

  // const {isFetching, error, dispatch} = useContext(AuthContext)


  const handleClick = async (e) => {
    e.preventDefault()
    setFieldError("")
    if(passwordAgain.current.value  !== password.current.value){
      passwordAgain.current.setCustomValidity("Password dont match")
    }
    else{
      const user = {
        username: username.current.value,
        email: email.current.value,
        password: password.current.value,
        confirm_password: passwordAgain.current.value
      };
      try{
        await axios.post(import.meta.env.VITE_API_URL + "/auth/signup/", user);
        navigate("/login")
      }
      catch(err){
        console.log(err.response.data.message)
        // console.log(err.response)
        setFieldError(err.response.data.message)
        
      }
    }


    // loginCall({username_or_email: email.current.value, password: password.current.value}, dispatch);
  }

  return (
    <div className="login">
      <div className="loginWrapper">
        <div className="loginLeft">
          <h3 className="loginLogo">Lamasocial</h3>
          <span className="loginDesc">
            Connect with friends and the world around you on Lamasocial.
          </span>
        </div>
        <div className="loginRight">
          <form className="loginBox" onSubmit={handleClick}>
            <h3 className="loginboxtitle">Create a new account</h3>
            <span className="field_error">{field_error}</span>
            <input placeholder="Username" required ref={username} className="loginInput" />
            <input placeholder="Email" type="email" required ref={email} className="loginInput" />
            <input placeholder="Password" minLength="6" type="password" required ref={password} className="loginInput" />
            <input placeholder="Password Again" minLength="6" type="password" required ref={passwordAgain} className="loginInput" />
            <button className="loginButton" type="submit">Sign Up</button>
            <button className="loginRegisterButton">
              Log into Account
            </button>
          </form>
        </div>
      </div>
    </div>
  );
}
