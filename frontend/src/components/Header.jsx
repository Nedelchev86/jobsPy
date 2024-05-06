import React from "react";
import {Link} from "react-router-dom";

export default function Header() {
    const isAuthenticated = localStorage.getItem("token");

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
                                        <Link to="/login" className="login">
                                            Login
                                        </Link>

                                        <Link to="/signup" className="btn">
                                            Sign Up
                                        </Link>
                                    </div>
                                )}
                            </nav>
                        </div>
                    </div>
                </div>
            </div>
        </header>
    );
}
