import React from "react";
import {Link} from "react-router-dom";

export default function Header() {
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
                                            {/* <a className="active" href="#">
                                                Home
                                            </a> */}
                                        </li>

                                        <li className="nav-item ">
                                            <a href="#" className="active">
                                                Jobs
                                            </a>
                                        </li>
                                        <li className="nav-item">
                                            <a href="#" className="">
                                                Companies
                                            </a>
                                        </li>
                                        <li className="nav-item">
                                            <a href="#" className="">
                                                Job Seekers
                                            </a>
                                        </li>
                                        <li className="nav-item">
                                            <Link to="/blog" className="nav-link">
                                                Blog
                                            </Link>
                                            {/* <a href="#" className="">
                                                Blog
                                            </a> */}
                                        </li>
                                        <li className="nav-item">
                                            <a href="#" className="">
                                                Contact
                                            </a>
                                        </li>
                                    </ul>
                                </div>

                                <div className="button">
                                    <a href="#" className="login">
                                        <i className="lni lni-lock-alt"></i> Login
                                    </a>
                                    <a href="#" className="btn">
                                        Sign Up
                                    </a>
                                    {/* <a href="#" className="login">
                                        <i className="lni lni-lock-alt"></i> Logout
                                    </a> */}
                                </div>
                            </nav>
                        </div>
                    </div>
                </div>
            </div>
        </header>
    );
}
