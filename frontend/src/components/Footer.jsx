export default function Footer() {
    return (
        <footer className="footer">
            <div className="footer-middle">
                <div className="container">
                    <div className="row">
                        <div className="col-lg-4 col-md-6 col-12">
                            <div className="f-about single-footer">
                                <div className="logo">
                                    <a href="index.html">
                                        <img src="/images/logo/logo.svg" alt="Logo" />
                                    </a>
                                </div>
                                <p>#1 project in SoftUni Django Advanced - February 2024</p>
                                <ul className="contact-address">
                                    <li>
                                        <span>Address:</span> 8000 Burgas , Bulgaria{" "}
                                    </li>
                                    <li>
                                        <span>Email:</span> t******.n******@gmail.com
                                    </li>
                                    <li>
                                        <span>Call:</span> 0899-899-899
                                    </li>
                                </ul>
                                <div className="footer-social">
                                    <ul>
                                        <li>
                                            <a href="https://bg-bg.facebook.com/tihomir.nedelchev" target="_blank">
                                                <i className="lni lni-facebook-original"></i>
                                            </a>
                                        </li>
                                        <li>
                                            <a href="#">
                                                <i className="lni lni-twitter-original"></i>
                                            </a>
                                        </li>
                                        <li>
                                            <a href="https://www.linkedin.com/in/tihomir-nedelchev/" target="_blank">
                                                <i className="lni lni-linkedin-original"></i>
                                            </a>
                                        </li>
                                        <li>
                                            <a href="https://github.com/Nedelchev86" target="_blank">
                                                <i className="lni lni-github-original"></i>
                                            </a>
                                        </li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                        <div className="col-lg-8 col-12">
                            <div className="row">
                                <div className="col-lg-4 col-md-6 col-12">
                                    <div className="single-footer f-link">
                                        <h3>For Job Seekers</h3>
                                        <ul>
                                            <li>
                                                <a href="login_redirect_dashboard">User Dashboard</a>
                                            </li>
                                            <li>
                                                <a href="#">Edit Profile</a>
                                            </li>
                                            <li>
                                                <a href="all_company">Companies</a>
                                            </li>
                                            <li>
                                                <a href="all-jobs">Jobs</a>
                                            </li>
                                            <li>
                                                <a href="favourite_jobs">Saved Jobs</a>
                                            </li>
                                        </ul>
                                    </div>
                                </div>
                                <div className="col-lg-4 col-md-6 col-12">
                                    <div className="single-footer f-link">
                                        <h3>For Companies</h3>
                                        <ul>
                                            <li>
                                                <a href="login_redirect_dashboard">Company Dashboard</a>
                                            </li>
                                            <li>
                                                <a href="create_job">Add Job Offer</a>
                                            </li>
                                            <li>
                                                <a href="all-employees">Job Seekers List</a>
                                            </li>
                                            <li>
                                                <a href="created-jobs">Created Jobs</a>
                                            </li>
                                            <li>
                                                <a href="jobs-applicants">Applicants</a>
                                            </li>
                                        </ul>
                                    </div>
                                </div>
                                <div className="col-lg-4 col-md-6 col-12">
                                    <div className="single-footer newsletter">
                                        <h3>Join Our Newsletter</h3>
                                        <p>Subscribe to get the latest news</p>
                                        {/* {% include 'core/subscription_form.html */}
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <div className="footer-bottom">
                <div className="container">
                    <div className="inner">
                        <div className="row">
                            <div className="col-lg-6 col-md-6 col-12">
                                <div className="left">
                                    <p>
                                        Django Project by
                                        <a href="#" rel="nofollow">
                                            Tihomir Nedelchev
                                        </a>
                                    </p>
                                </div>
                            </div>
                            <div className="col-lg-6 col-md-6 col-10">
                                <div className="right">
                                    <ul>
                                        <li>
                                            <a href="#">Terms of use</a>
                                        </li>
                                        <li>
                                            <a href="#"> Privacy Policy</a>
                                        </li>
                                        <li>
                                            <a href="#">Faq</a>
                                        </li>
                                        <li>
                                            <a href="contact">Contact</a>
                                        </li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </footer>
    );
}
