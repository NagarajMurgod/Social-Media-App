import { useContext } from "react";
import Home from "./pages/home/Home";
import Login from "./pages/login/Login";
import Profile from "./pages/profile/Profile";
import Register from "./pages/register/Register";
import {
  BrowserRouter as Router,
  Routes,
  Route,
  Navigate
} from "react-router-dom";
import { AuthContext } from "./context/AuthContext";

function App() {
  const {user} = useContext(AuthContext)
  console.log(user);
  return (
    <>
      <Router>
        <Routes>
          <Route path="/login" element={ user ? <Navigate to="/" /> :  <Login/> } />
          {/* <Route path="/" element={ user ? <Home/> : <Register/> } /> */}
          <Route path="/" element={ user ? <Home/> : <Login/> } />
          <Route path="/register" element={ user ? <Navigate to="/" /> : <Register/>} />
          <Route path="/profile/:user_id" element={ user ? <Profile/> : <Navigate to="/" />} />
        </Routes>
      </Router>
    </>
  )
}

export default App
