import React from "react";
import {Link, Outlet} from "react-router-dom";

const Breadcrumbs = ({pageTitle, pageInfo}) => {
    return (
        <>
            <div className="breadcrumbs overlay">
                <div className="container">
                    <div className="row">
                        <div className="col-12">
                            <div className="breadcrumbs-content">
                                <h1 className="page-title">{pageTitle}</h1>
                                <p>{pageInfo}</p>
                            </div>
                            <ul className="breadcrumb-nav">
                                <li>
                                    <Link href="/">Home</Link>
                                </li>
                                <li>Companies</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
            {/* <Outlet /> */}
        </>
    );
};

export default Breadcrumbs;
