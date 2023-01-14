'use client';

import { useRouter } from 'next/navigation';
import API_CALLS from '../../app/api/api_routes';
import React, { useState, useEffect } from 'react';


export default function Form() {

    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [errorMessage, setErrorMessage] = useState("");
    const [rememberMe, setRememberMe] = useState(false);
    const [isLoading, setIsLoading] = useState(false);
    const [hasMounted, setHasMounted] = useState(false);
    const [isloaded, setIsloaded] = useState(false);

    let router = undefined;

    useEffect(() => {
        setHasMounted(true);
        setTimeout(() => {
            setIsloaded(true);
        }, 1500);
    }, []);

    const _handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const data = await API_CALLS.loginUser(username, password);
            if (data.message && data.status_code) {
                console.log(data.message, data.status_code);
                window.localStorage.setItem("token", data.access_token);
                setTimeout(() => { router.push("/"); }, 1000);
            } else {
                setErrorMessage(data.message);
            }
        } catch (error) {
            console.log(error);
        }
    }

    if (!hasMounted) {
        return null;
    } else {
        router = useRouter();
    }


    return (
        <form onSubmit={_handleSubmit} style={{ display: isloaded ? "flex" : "none", width: isloaded ? "50%" : "0%" }}>
            <span style={{ fontSize: 30, marginBottom: 50 }}>Welcome Back</span>
            <div className="username">
                <label style={{ fontSize: 16, color: "#ccc", paddingBottom: 5, }} htmlFor="usernameInput">Username</label>
                <input name="username" type="text" id="usernameInput" placeholder="Pick username" 
                    onChange={(e) => setUsername(e.target.value)} 
                />
            </div>
            <div className="password">
                <label style={{ fontSize: 16, paddingBottom: 5, color: "#ccc" }} htmlFor="passwordInput">Password</label>
                <input name="password" type="password" id="passwordInput" className="form-control" placeholder="Enter Password" 
                    onChange={(e) => setPassword(e.target.value)} 
                />
            </div>
            <div className='remember_me'>
                <a style={{ fontSize: 16, color: "#457b9d", cursor: "pointer"}}>Forgot password?</a>
            </div>
            <div className='button'>
                <button disabled={isLoading}>SIGN IN</button>
            </div>
        </form>
    )
}