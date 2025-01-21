import { useContext, useRef } from "react";
import "./login.css";
import { loginCall } from "../../apiCalls";
import { AuthContext} from "../../context/AuthContext"
import CircularProgress from '@mui/material/CircularProgress';
import { CSRFToken } from "../../components/CSRF_token";

export default function Login() {

  const email = useRef();
  const password = useRef();
  const {isFetching, error, dispatch} = useContext(AuthContext)


  const handleClick = (e) => {
    e.preventDefault()
    loginCall({username_or_email: email.current.value, password: password.current.value}, dispatch);
    
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
            <CSRFToken/>
            <h3 className="loginboxtitle">Log in to Facebook</h3>
            <input type="email" required placeholder="Email" className="loginInput" ref={email}/>
            <input type="password" required placeholder="Password" className="loginInput" ref={password} />
            <button className="loginButton" disabled = {isFetching}>{isFetching ? <CircularProgress color="white" size="20px"  /> : "Login In"}</button>
            <span className="loginForgot">Forgot Password?</span>
            <button className="loginRegisterButton">
              Create a New Account
            </button>
          </form>
        </div>
      </div>
    </div>
  );
}
