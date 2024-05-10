// RegisterForm.js
import React, {useState} from "react";
import Breadcrumbs from "./Breadcrumbs";
import {useNavigate} from "react-router-dom";

const RegisterForm = () => {
    const navigate = useNavigate();
    const [formData, setFormData] = useState({
        email: "",
        password: "",
        password2: "",
        role: "", // Default role
    });
    const [error, setError] = useState("");

    const handleChange = (e) => {
        setFormData({...formData, [e.target.name]: e.target.value});
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            // Check if passwords match
            if (formData.password !== formData.password2) {
                throw new Error("Passwords do not match");
            }

            const response = await fetch("http://127.0.0.1:8000/api/register/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(formData),
            });

            if (!response.ok) {
                // Check if email already exists
                const responseData = await response.json();
                if (responseData.email) {
                    throw new Error("Email already exists");
                }
                throw new Error("Registration failed");
            }
            navigate("/");
            console.log("User registered successfully");
            // Redirect or show success message
        } catch (error) {
            console.error("Registration failed:", error.message);
            setError(error.message); // Set error message for display
            // Handle error (e.g., display error message)
        }
    };
    return (
        <>
            <Breadcrumbs
                pageTitle="Sing Up"
                pageInfo="JobsPy It helps you to increase your chances of finding a suitable job<br> disciplines.
                            and let recruiters contact you about jobs that are not needed to pay for advertising."
            />

            <section className="about-us section">
                <div className="container">
                    <div className="row  justify-content-center">
                        <div className="col-lg-6 col-md-10 col-12">
                            <div className="content-left wow fadeInLeft" data-wow-delay=".3s">
                                <div calss="row">
                                    <div className="col-lg-6 col-12">
                                        <div className="row">
                                            <div className="col-lg-6 col-md-6 col-6">
                                                <img className="single-img" src="/images/about/small1.jpg" alt="#" />
                                            </div>
                                            <div className="col-lg-6 col-md-6 col-6">
                                                <img className="single-img mt-50" src="/images/about/small2.jpg" alt="#" />
                                            </div>
                                        </div>
                                    </div>
                                    <div className="col-lg-6 col-12">
                                        <div className="row">
                                            <div className="col-lg-6 col-md-6 col-6">
                                                <img className="single-img minus-margin" src="/images/about/small3.jpg" alt="#" />
                                            </div>
                                            <div className="col-lg-6 col-md-6 col-6">
                                                <div className="media-body">
                                                    <i className="lni lni-checkmark"></i>
                                                    <h6 className="">Sing Up!</h6>
                                                    <p className="">Join the JobsPy community</p>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div className="col-lg-6 col-md-10 col-12">
                            <div className="login-information">
                                <h3 className="title title-margin">Registration</h3>
                                <form onSubmit={handleSubmit}>
                                    <div className="row">
                                        {error && <div className="alert alert-danger">{error}</div>} {/* Render error message if present */}
                                        <div className="form-group">
                                            <label htmlFor="id_email">Email:</label>
                                            <input type="email" name="email" maxLength="100" autoFocus className="form-control" placeholder="Enter your email" value={formData.email} onChange={handleChange} required id="id_email" />
                                        </div>
                                        <div className="form-group">
                                            <label htmlFor="id_password">Password:</label>
                                            <input type="password" name="password" autoComplete="new-password" className="form-control" placeholder="Enter your password" value={formData.password} onChange={handleChange} required aria-describedby="id_password1_helptext" id="id_password" />
                                        </div>
                                        <div className="form-group">
                                            <label htmlFor="id_password2">Password confirmation:</label>
                                            <input type="password" name="password2" autoComplete="new-password" className="form-control" placeholder="Enter your password" value={formData.password2} onChange={handleChange} required aria-describedby="id_password2_helptext" id="id_password2" />
                                        </div>
                                        <div className="form-group">
                                            <label htmlFor="id_role">Profile type:</label>
                                            <select name="role" className="form-control" value={formData.role} onChange={handleChange} required id="id_role">
                                                <option value="">---------</option>
                                                <option value="jobseeker">Job Seeker</option>
                                                <option value="company">Company</option>
                                            </select>
                                        </div>
                                        <div className="col-lg-12 button">
                                            <button className="btn" type="submit">
                                                Register
                                            </button>
                                        </div>
                                    </div>
                                </form>
                            </div>
                            <a className="google" href="{% provider_login_url 'google' %}">
                                Login with Google
                            </a>
                            <a className="github" href="{% provider_login_url 'github' %}">
                                Login with GitHun
                            </a>
                        </div>
                    </div>
                </div>
            </section>

            <section className="apply-process section">
                <div className="container">
                    <div className="row">
                        <div className="col-lg-4 col-md-4 col-12">
                            <div className="process-item">
                                <i className="lni lni-user"></i>
                                <h4>Register Your Account</h4>
                                <p>Lorem Ipsum is simply dummy text of the printing and typesetting industry.</p>
                            </div>
                        </div>
                        <div className="col-lg-4 col-md-4 col-12">
                            <div className="process-item">
                                <i className="lni lni-book"></i>
                                <h4>Upload Your Resume</h4>
                                <p>Lorem Ipsum is simply dummy text of the printing and typesetting industry.</p>
                            </div>
                        </div>
                        <div className="col-lg-4 col-md-4 col-12">
                            <div className="process-item">
                                <i className="lni lni-briefcase"></i>
                                <h4>Apply for Dream Job</h4>
                                <p>Lorem Ipsum is simply dummy text of the printing and typesetting industry.</p>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
        </>
    );
};

export default RegisterForm;
