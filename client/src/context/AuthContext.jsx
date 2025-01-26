import { createContext, useReducer } from "react";
import AuthReducer from "./AuthReducer";


const storedUser = localStorage.getItem('user');

const INITIAL_STATE = {
    user: JSON.parse(storedUser),
    isFetching: false,
    error : false
};


export const AuthContext = createContext(INITIAL_STATE);

export const AuthContextProvider = ({children}) => {
    const [state, dispatch] = useReducer(AuthReducer,INITIAL_STATE);

    if(state.user && !state.error){
        localStorage.setItem("user",JSON.stringify(state.user));
    }
    
    return (
        <AuthContext.Provider value = {{user:state.user, isFetching: state.isFetching,error: state.error, dispatch}}>
        {children}
        </AuthContext.Provider>
    );
}