import axios from "axios";
import { useEffect, useState } from "react"


export const CSRFToken = () => {
    const [csrftoken, setCsrfToken] = useState("");

    const getCookie = (key) => {
        let cookieValue = null;
        if(document.cookie && document.cookie !== ''){
            let cookies = document.cookie.split(";");
            for(let i=0; i<cookies.length;i++){
                let cookie = cookies[i].trim();
                
                if(cookie.substring(0, key.length+1) === (key+"=")){
                    cookieValue = decodeURIComponent(cookie.substring(0, key.length+1));
                    break;
                }
            }
        }
        return cookieValue
    
    }
    
    
    useEffect(()=>{
        const fetchData = async () => {
            try{
                
                const r = await axios.get(`${import.meta.env.VITE_API_URL}/auth/csrf_cookie/`,{withCredentials:true});
                console.log(r.data);
            }
            catch(err){
                console.log(err);
            }
        };

        fetchData();
        setCsrfToken(getCookie('csrftoken'));
    },[]);

    return (
        <input type="hidden" name="csrfmiddlewaretoken" value={csrftoken}/>
    )
}
