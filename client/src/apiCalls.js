import axios from "axios"

export const loginCall = async (userCreds, dispatch) => {
    dispatch({type: "LOGIN_START"});
    try{
        const res = await axios.post("http://127.0.0.1:8000/auth/login/", userCreds);
        console.log(res.data)
        dispatch({type : "LOGIN_SUCCESS", payload : res.data});
    }
    catch(err){
        dispatch({type : "LOGIN_FAILURE", payload : err});
    }
}
