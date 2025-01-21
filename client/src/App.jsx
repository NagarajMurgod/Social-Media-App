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
  return (
    <>
      <Router>
        <Routes>
          <Route path="/login" element={ user ? <Navigate to="/" /> :  <Login/> } />
          {/* <Route path="/" element={ user ? <Home/> : <Register/> } /> */}
          <Route path="/" element={ <Home/> } />
          <Route path="/register" element={ user ? <Navigate to="/" /> : <Register/>} />
          <Route path="/profile" element={<Profile/>} />
        </Routes>
      </Router>
    </>
  )
}

export default App
