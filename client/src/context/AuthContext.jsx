import { createContext, useReducer } from "react";
import AuthReducer from "./AuthReducer";

const INITIAL_STATE = {
    user: {
        "status": "success",
        "message": "Login successful",
        "payload": {
            "id": 1,
            "username": "nagaraj",
            "first_name": "Nagaraj12",
            "last_name": "Murgod",
            "date_joined": "2024-12-16T14:08:02.663920Z",
            "profile_img": "/media/users/1/profile_images/1.png"
        }
    },
    isFetching: false,
    error : false
};

export const AuthContext = createContext(INITIAL_STATE);


export const AuthContextProvider = ({children}) => {
    const [state, dispatch] = useReducer(AuthReducer,INITIAL_STATE);

    return (
        <AuthContext.Provider value = {{user:state.user, isFetching: state.isFetching,error: state.error, dispatch}}>
        {children}
        </AuthContext.Provider>
    );
}