import {useEffect, useState} from "react";
import Breadcrumbs from "./Breadcrumbs";

export default function JobseekersList() {
    const [jobseekers, setJobseekers] = useState([]);
    useEffect(() => {
        fetch("http://127.0.0.1:8000/jobseeker/jobseekers/")
            .then((response) => response.json())
            .then((data) => setJobseekers(data));
    });
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
                                                    <a href="{% url 'jobseeker details' jobseeker.pk %}">
                                                        {jobseeker.first_name} {jobseeker.last_name}
                                                    </a>
                                                </h3>
                                                <span className="deg">{jobseeker.occupation}</span>
                                                <ul className="experience">
                                                    <li>
                                                        Seniority: <span>{jobseeker.seniority}</span>
                                                    </li>

                                                    <li>
                                                        GitHub:{" "}
                                                        <span>
                                                            <a target="_blank" href="{ jobseeker.github }">
                                                                Link
                                                            </a>
                                                        </span>
                                                    </li>

                                                    <li>
                                                        <i className="lni lni-map-marker"></i>
                                                        {jobseeker.city}
                                                    </li>
                                                </ul>
                                                <ul className="skills">
                                                    {/* {% for skill in jobseeker.skills.all %}
                                                                        <li>{{ skill.name }}</li>
                                
                                                                            {% endfor %} */}
                                                </ul>
                                            </div>
                                        </div>
                                    ))}
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </>
    );
}
