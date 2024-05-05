import React, {useEffect, useState} from "react";
import Breadcrumbs from "./Breadcrumbs";
import JobSeekersAside from "./JobseekersAside";
import {Link} from "react-router-dom";

export default function JobseekersList() {
    const [jobseekers, setJobseekers] = useState([]);
    const [city, setCity] = useState("");

    useEffect(() => {
        const params = new URLSearchParams(window.location.search);
        const cityParam = params.get("city");
        if (cityParam) {
            setCity(cityParam);
        }
    }, []);

    useEffect(() => {
        fetch(`http://127.0.0.1:8000/jobseeker/jobseekers/?city=${city}`)
            .then((response) => response.json())
            .then((data) => setJobseekers(data));
    }, [city]);

    return (
        <>
            <Breadcrumbs pageTitle="Job Seekers" pageInfo="Find employees that match your hiring criteria." />

            <div className="manage-resumes section">
                <div className="container">
                    <div className="resume-inner">
                        <div className="row">
                            <div className="col-lg-8 col-12">
                                <div className="inner-content">
                                    {jobseekers.map((jobseeker) => (
                                        <div key={jobseeker.user} className="resume-item">
                                            <img src={`https://res.cloudinary.com/drjgddl0y/${jobseeker.profile_picture}`} alt="Candidate" />
                                            <div className="right">
                                                <h3>
                                                    <Link to={`/jobseeker/${jobseeker.user}`}>
                                                        {jobseeker.first_name} {jobseeker.last_name}
                                                    </Link>
                                                </h3>
                                                <span className="deg">{jobseeker.occupation}</span>
                                                <ul className="experience">
                                                    <li>
                                                        Seniority: <span>{jobseeker.seniority}</span>
                                                    </li>
                                                    <li>
                                                        GitHub:{" "}
                                                        <span>
                                                            <a target="_blank" href="{jobseeker.github}">
                                                                Link
                                                            </a>
                                                        </span>
                                                    </li>
                                                    <li>
                                                        <i className="lni lni-map-marker"></i>
                                                        {jobseeker.city}
                                                    </li>
                                                </ul>
                                                <ul className="skills">{/* Render jobseeker skills */}</ul>
                                            </div>
                                        </div>
                                    ))}
                                </div>
                            </div>
                            <JobSeekersAside />
                        </div>
                    </div>
                </div>
            </div>
        </>
    );
}
