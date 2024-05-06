import {useState, useEffect} from "react";
import Breadcrumbs from "./Breadcrumbs";
import JobSeekersAside from "./JobseekersAside";
import {useParams} from "react-router-dom";

export default function JobSeekerDetails() {
    const [jobseeker, setJobseeker] = useState([]);
    const {id} = useParams();

    useEffect(() => {
        console.log("Start useEffect with ID:", id);
        fetch(`http://127.0.0.1:8000/jobseeker/jobseekers/${id}/`)
            .then((response) => response.json())
            .then((data) => {
                setJobseeker(data);
            })
            .catch((error) => console.error("Error fetching jobseeker:", error));
    }, [id]);
    console.log(jobseeker);

    return (
        <>
            <Breadcrumbs
                pageTitle="Resume"
                pageInfo="Don’t just find. Be found. Put your CV in front of great employers<br> 
    t helps you to increase your chances of finding a suitable job and let recruiters contact you about jobs that are not needed to pay for advertising"
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
                                                                {jobseeker.profile_picture && (
                                                                    <a className="mb-2" href="#">
                                                                        <img className="circle-54" src={`https://res.cloudinary.com/drjgddl0y/${jobseeker.profile_picture}`} alt="" />
                                                                    </a>
                                                                )}

                                                                {/* <h4>{jobseeker.first_nam}</h4> */}
                                                                <p>{jobseeker.occupation}</p>
                                                                <ul className="social">
                                                                    {/* <li>
                                                                        <a target="_blank" href="{ jobseeker.facebook }">
                                                                            <i className="lni lni-facebook-original"></i>
                                                                        </a>
                                                                    </li>

                                                                    <li>
                                                                        <a target="_blank" href="{{ jobseeker.linkedin }}">
                                                                            <i className="lni lni-linkedin-original"></i>
                                                                        </a>
                                                                    </li>

                                                                    <li>
                                                                        <a target="_blank" href="{{ jobseeker.github }}">
                                                                            <i className="lni lni-github"></i>
                                                                        </a>
                                                                    </li> */}
                                                                </ul>
                                                            </div>
                                                        </div>
                                                        <div className="col-lg-7 col-md-7 col-12">
                                                            <div className="content-right">
                                                                <h5 className="title-main">Contact Info</h5>

                                                                <div className="single-list">
                                                                    <h5 className="title">Location</h5>
                                                                    <p>{jobseeker.city} </p>
                                                                </div>

                                                                <div className="single-list">
                                                                    <h5 className="title">E-mail</h5>
                                                                    <p>{jobseeker.id}</p>
                                                                </div>

                                                                <div className="single-list">
                                                                    <h5 className="title">Phone</h5>
                                                                    <p>{jobseeker.phone_number}</p>
                                                                </div>

                                                                <div className="single-list">
                                                                    <h5 className="title">Website</h5>

                                                                    <p>
                                                                        {/* <a target="_blank" href="{{ jobseeker.website }}">
                                                                            Link
                                                                        </a> */}
                                                                    </p>
                                                                </div>

                                                                <div className="single-list">
                                                                    <h5 className="title">Seniority</h5>
                                                                    <p>{jobseeker.seniority}</p>
                                                                </div>

                                                                <div className="single-list">
                                                                    <h5 className="title">Phone</h5>
                                                                    <p> Hidden </p>
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>

                                                <div className="single-section">
                                                    <h4>About</h4>
                                                    <p className="font-size-4 mb-8">{jobseeker.about}</p>
                                                </div>

                                                <div className="single-section skill">
                                                    <h4>Skills</h4>
                                                    <ul className="list-unstyled d-flex align-items-center flex-wrap">
                                                        {/* {%  for skill in jobseeker.skills.all %}
                                    <li>
                                        <a href="#">{{ skill }}</a>
                                    </li>
                                    {% endfor %} */}
                                                    </ul>
                                                </div>

                                                <div className="single-section exprerience">
                                                    <h4>Work Experience</h4>
                                                    {/* {% for experience in jobseeker.experience.all %}
                                <div className="single-exp mb-30">
                                    <div className="d-flex align-items-center pr-11 mb-9 flex-wrap flex-sm-nowrap">
                                        <div className="image">
                                            {% if experience.image %}
                                                <img width="80" height="80"  src="{{ experience.image }}"  alt="#">
                                            {% else %}
                                             <img width="80" height="80"  src="{% static 'images/resume/work.jpg' %}"  alt="#">
                                            {% endif %}
                                        </div>
                                        <div className="w-100 mt-n2">
                                            <h3 className="mb-0">
                                                <h5>{{ experience.company}}</h5>
                                            </h3>
                                            <p>{{ experience.description|safe }}</p>
                                            <div className="d-flex align-items-center justify-content-md-between flex-wrap">
                                                <p>{{ experience.start_date}} - {{ experience.end_date}}</p>
{#                                                <a href="#" className="font-size-3 text-gray">#}
{#                                                    <span className="mr-2" style="margin-top: -2px"><i#}
{#                                                            className="lni lni-map-marker"></i></span>New York, USA</a>#}
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                {% endfor %} */}
                                                </div>

                                                <div className="single-section education">
                                                    <h4>Education</h4>

                                                    {/* {% for education in jobseeker.educations.all %}
                                <div className="single-edu mb-30">
                                    <div className="d-flex align-items-center pr-11 mb-9 flex-wrap flex-sm-nowrap">
                                        <div className="image">
                                            {% if education.image %}
                                                 <img width="80" height="80"  src="{{ education.image }}"  alt="#">
                                            {% else %}
                                            <img width="80" height="80" src="{% static '/images/resume/education.jpg' %}" alt="#">
                                            {% endif %}
                                        </div>
                                        <div className="w-100 mt-n2">
                                            <h3 className="mb-0">
                                                <h5>{{ education.institution}}</h5>
                                            </h3>
                                            <p>{{  education.description|safe }}</p>
                                            <div className="d-flex align-items-center justify-content-md-between flex-wrap">
                                                <p>{{ education.start_date}} - {{  education.end_date}}</p>
                                               
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                {% endfor %} */}
                                                </div>
                                            </div>
                                        </div>
                                        <JobSeekersAside />
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
