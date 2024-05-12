import {useState, useEffect} from "react";
import Breadcrumbs from "./Breadcrumbs";
import {useParams} from "react-router-dom";

export default function CompanyDetails() {
    const [company, setCompany] = useState();
    const {id} = useParams();

    useEffect(() => {
        fetch(`http://127.0.0.1:8000/company/api/companies/${id}/`)
            .then((response) => response.json())
            .then((data) => {
                setCompany(data);
            })
            .catch((error) => console.error("Error fetching jobseeker:", error));
    }, [id]);

    if (!company) {
        // Render loading state or redirect to login page
        console.log("loading");
        return <div>Loading...</div>;
    }

    return (
        <>
            <Breadcrumbs
                pageTitle="Company Details"
                pageInfo="Business plan draws on a wide range of knowledge from different business<br> disciplines.
                            Business draws on a wide range of different business ."
            />
            <section className="section blog-single">
                <div className="container">
                    <div className="row">
                        <div className="resume ">
                            <div className="container">
                                <div className="resume-inner">
                                    <div className="row">
                                        <div className="col-lg-8 col-12">
                                            <div className="inner-content">
                                                <div className="personal-top-content">
                                                    <div className="row">
                                                        <div className="col-lg-5 col-md-5 col-12">
                                                            <div className="name-head">
                                                                <a className="mb-2" href="#">
                                                                    <img className="circle-54" src={`https://res.cloudinary.com/drjgddl0y/${company.image}`} alt="" />
                                                                </a>

                                                                <h4>
                                                                    <a className="name" href="#">
                                                                        {company.name}
                                                                    </a>
                                                                </h4>

                                                                <ul className="social">
                                                                    <li>
                                                                        <a href="{{ company.facebook_url }}">
                                                                            <i className="lni lni-facebook-original"></i>
                                                                        </a>
                                                                    </li>

                                                                    <li>
                                                                        <a target="_blank" href="{{ company.linkedin_url }}">
                                                                            <i className="lni lni-linkedin-original"></i>
                                                                        </a>
                                                                    </li>
                                                                </ul>
                                                            </div>
                                                        </div>
                                                        <div className="col-lg-7 col-md-7 col-12">
                                                            <div className="content-right">
                                                                <h5 className="title-main">Contact Info</h5>
                                                                <div className="single-list">
                                                                    <h5 className="title">Location</h5>
                                                                    <p>{company.location}</p>
                                                                </div>
                                                                <div className="single-list">
                                                                    <h5 className="title">E-mail</h5>
                                                                    <p>{company.email}</p>
                                                                </div>

                                                                <div className="single-list">
                                                                    <h5 className="title">Phone</h5>
                                                                    <p>{company.phone}</p>
                                                                </div>

                                                                <div className="single-list">
                                                                    <h5 className="title">Address</h5>
                                                                    <p>{company.address}</p>
                                                                </div>
                                                                <div className="single-list">
                                                                    <h5 className="title">Employees</h5>
                                                                    <p>{company.employees}</p>
                                                                </div>
                                                                <div className="single-list">
                                                                    <h5 className="title">Foundation Year</h5>
                                                                    <p>{company.foundation_year}</p>
                                                                </div>

                                                                <div className="single-list">
                                                                    <h5 className="title">Website Linked</h5>
                                                                    <p>
                                                                        <a target="_blank" href="{{ company.website_url }}">
                                                                            {" "}
                                                                            Link{" "}
                                                                        </a>
                                                                    </p>
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>

                                                <div className="single-section">
                                                    <h4>About</h4>
                                                    <p className="font-size-4 mb-8">{company.description}</p>
                                                </div>

                                                <div className="single-section skill">
                                                    <h4>Technologies</h4>
                                                    <ul className="list-unstyled d-flex align-items-center flex-wrap">
                                                        {company &&
                                                            company.skills &&
                                                            company.skills.map((tech) => (
                                                                <li key={tech}>
                                                                    <a href="#">{tech}</a>
                                                                </li>
                                                            ))}

                                                        {/* {{ company.skills_set }}
                                    {% for tech in company.skills.all %}
                                    <li>
                                        <a href="#">{{ tech }}</a>
                                    </li>
                                {% endfor %} */}
                                                    </ul>
                                                </div>
                                                <div className="single-section">
                                                    <h4>Open positions </h4>
                                                    <div className="job-items">
                                                        {/* {% for job in jobs_published %}
                            <div className="manage-content" style="margin-top: 16px">
                                <div className="row align-items-center justify-content-center">
                                    <div className="col-lg-6 col-md-6 col-12">
                                        <div className="title-img" style="display: flex">
                                            <div className="can-img">
                                                {% if job.job_image %}
                                                <img style="height: 60px; width: 60px;" src="{{ job.job_image.url }}" alt="#">
                                                    {% else %}
                                                    <img style="height: 60px; width: 60px;" src="{{ company.image.url }}" alt="#">
                                                {% endif %}
                                            </div>
                                            <h6  style="padding-left: 10px">{{ job.title }}</h6>
                                                <span style="text-align: right">{{ job.category}}</span>
                                        </div>
                                    </div>
                                    <div className="col-lg-2 col-md-2 col-12">
                                        <p><span className="time"><i className="lni lni-coin"></i> {{ job.salary }}</span></p>
                                    </div>
                                    <div className="col-lg-2 col-md-2 col-12">
                                        <p className="location"><i className="lni lni-map-marker"></i>{{job.location}}</p>
                                    </div>
                                    <div className="col-lg-2 col-md-2 col-12">
                                        <div className="button">
                                            <a href="{% url 'job_details' job.pk %}" className="btn">Details</a>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            {% endfor %} */}
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
        </>
    );
}
