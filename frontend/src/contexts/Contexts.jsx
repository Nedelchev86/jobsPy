// import React, { createContext, useState, useContext } from "react";

// const AuthContext = createContext();

// export const AuthProvider = ({ children }) => {
//   const [isAuthenticated, setIsAuthenticated] = useState(false);

//   const login = () => {
//     // Perform authentication logic here (e.g., make API call to validate credentials)
//     // If authentication is successful, set isAuthenticated to true
//     setIsAuthenticated(true);
//   };

//   const logout = () => {
//     // Perform logout logic here (e.g., clear session, remove tokens)
//     setIsAuthenticated(false);
//   };

//   return (
//     <AuthContext.Provider value={{ isAuthenticated, login, logout }}>
//       {children}
//     </AuthContext.Provider>
//   );
// };

// export const useAuth = () => useContext(AuthContext);

import React, {createContext, useContext, useEffect, useState} from "react";
import {useNavigate} from "react-router-dom";

const AuthContext = createContext();

export const AuthProvider = ({children}) => {
    const [user, setUser] = useState(null);
    const [token, setToken] = useState(localStorage.getItem("token"));

    const isAuthenticated = !!token;
    console.log(isAuthenticated);
    const history = useNavigate();

    const login = async (formData) => {
        try {
            const response = await fetch("http://127.0.0.1:8000/api/token/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(formData),
            });

            if (!response.ok) {
                throw new Error("Invalid email or password");
            }
            const data = await response.json();
            localStorage.setItem("token", data.access); // Store token in local storage
            localStorage.setItem("refresh_token", data.refresh);
            setToken(data.access);
            setUser(response.data);
            console.log(user);
        } catch (error) {
            console.error("Login failed:", error.message);
            setError(error.message);
        }
    };

    useEffect(() => {
        if (!isAuthenticated) {
            return;
        }

        fetch("http://127.0.0.1:8000/api/user/", {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
                Authorization: `Bearer ${token}`,
            },
        })
            .then((response) => {
                if (!response.ok) {
                    throw new Error("Failed to fetch user data");
                }
                return response.json();
            })
            .then((data) => {
                setUser(data);
            })
            .catch((error) => {
                console.error("Error fetching user data:", error);
            });
    }, [isAuthenticated]);

    const logout = () => {
        localStorage.removeItem("token");
        setToken(null);
        history("/");
    };

    return <AuthContext.Provider value={{user, isAuthenticated, login, logout}}>{children}</AuthContext.Provider>;
};

export const useAuth = () => useContext(AuthContext);
