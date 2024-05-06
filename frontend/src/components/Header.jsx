import React, {useState, useEffect} from "react";
import {Link, useNavigate} from "react-router-dom";

import LoginModal from "./LoginForm";
import {jwtDecode} from "jwt-decode";

export default function Header() {
    const isAuthenticated = localStorage.getItem("token");
    const [user, setUser] = useState(null);
    const history = useNavigate();
    const [showModal, setShowModal] = useState(false);
    const toggleModal = () => {
        setShowModal(!showModal);
    };

    const handleLogout = () => {
        localStorage.removeItem("token");
        history("/");
    };

    useEffect(() => {
        if (!isAuthenticated) {
            return;
        }

        fetch("http://127.0.0.1:8000/api/user/", {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
                Authorization: `Bearer ${isAuthenticated}`,
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
    }, []);

    return (
        <header className="header style4">
            <div className="navbar-area">
                <div className="container">
                    <div className="row align-items-center">
                        <div className="col-lg-12">
                            <nav className="navbar navbar-expand-lg">
                                <a className="navbar-brand logo" href="#">
                                    <img className="logo1" src="/images/logo/logo.svg" alt="Logo" />
                                </a>
                                <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                                    <span className="toggler-icon"></span>
                                    <span className="toggler-icon"></span>
                                    <span className="toggler-icon"></span>
                                </button>

                                <div className="collapse navbar-collapse sub-menu-bar" id="navbarSupportedContent">
                                    <ul id="nav" className="navbar-nav ml-auto">
                                        <li className="nav-item">
                                            <Link to="/" className="nav-link">
                                                Home
                                            </Link>
                                        </li>

                                        <li className="nav-item ">
                                            <Link to="/jobs" className="nav-link">
                                                Jobs
                                            </Link>
                                        </li>
                                        <li className="nav-item">
                                            <Link to="/companies" className="nav-link">
                                                Companies
                                            </Link>
                                        </li>
                                        <li className="nav-item">
                                            <Link to="/jobseekers" className="nav-link">
                                                Jobseekers
                                            </Link>
                                        </li>
                                        <li className="nav-item">
                                            <Link to="/blog" className="nav-link">
                                                Blog
                                            </Link>
                                        </li>
                                        <li className="nav-item">
                                            <a href="#" className="">
                                                Contact
                                            </a>
                                        </li>
                                    </ul>
                                </div>

                                {!isAuthenticated && (
                                    <div className="button">
                                        {/* <Link to="/login" className="login">
                                            Login
                                        </Link> */}
                                        <Link onClick={toggleModal} className="login">
                                            <i className="lni lni-lock-alt"></i>
                                            Login
                                        </Link>

                                        <Link to="/signup" className="btn">
                                            Sign Up
                                        </Link>
                                    </div>
                                )}

                                {isAuthenticated && (
                                    <>
                                        <div
                                            className="text-center align-center"
                                            style={{
                                                alignItems: "center !important",
                                                justifyContent: "center !important",
                                                backgroundColor: "black",
                                                width: 50,
                                                height: 50,
                                                borderRadius: 50,
                                                marginRight: 10,
                                                marginLeft: 20,
                                            }}
                                        >
                                            <div className="user-profile-container">
                                                {/* <a href="#">
                                                <img className="user-profile-small" src="" alt="Logo" /> <span className="notification-badge">0</span>
                                            </a> */}
                                                {user && (
                                                    <a href="#" className="user-profile-small" style={{paddingTop: "10%", color: "white", fontSize: 25}}>
                                                        {user.email.split("")[0]}
                                                        <span className="notification-badge">0</span>
                                                    </a>
                                                )}
                                            </div>
                                        </div>
                                        <div className="button">
                                            <button onClick={handleLogout} className="btn">
                                                Logout
                                            </button>
                                        </div>
                                    </>
                                )}
                            </nav>
                        </div>
                    </div>
                </div>
            </div>
            <LoginModal show={showModal} handleClose={toggleModal} />
        </header>
    );
}
