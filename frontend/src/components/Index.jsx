export default function Index() {
    return (
        <>
            <section className="hero-area style4">
                <div className="hero-inner">
                    <div className="container">
                        <div className="row ">
                            <div className="col-lg-10 offset-lg-1 co-12">
                                <div className="inner-content">
                                    <div className="hero-text">
                                        {/* {% if messages %}
                                    {{ message }}
    <div className="alert alert-danger" role="alert">
        
        <ul className="messages">
            {% for message in messages %}
            <li>{{ message }}</li>
            {% endfor %}
        </ul>
    </div>
    {% endif %} */}
                                        <h1 className="wow fadeInUp" data-wow-delay=".3s">
                                            Find a job you love,
                                            <br /> and you will never have to work a day in your life.
                                        </h1>
                                        <p className="wow fadeInUp" data-wow-delay=".5s">
                                            What do you seek? Whether it’s a work-from-home role or a bigger salary, we’ll help you find the right job. There’s no secret – just better job matches than ever before. Seek and you shall find.
                                        </p>
                                        <div className="button wow fadeInUp" data-wow-delay=".7s">
                                            {/* {% if user.company %} */}
                                            {/* <a href="{% url "create_job" %}" className="btn">Post a Job</a> */}
                                            {/* {% endif %} */}
                                            <a href="#" className="btn btn-alt">
                                                See Our Jobs
                                            </a>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div className="row">
                            <div className="col-12">
                                <div className="index-counter">
                                    <div className="ftco-counter ftco-no-pt ftco-no-pb">
                                        <div className="row">
                                            <div className="col-md-4 d-flex justify-content-center counter-wrap ftco-animate">
                                                <div className="block-18">
                                                    <div className="text d-flex">
                                                        <div className="icon mr-2">
                                                            <span className="flaticon-worldwide"></span>
                                                        </div>
                                                        <div className="desc text-left">
                                                            <strong className="numberAnimated" data-number="12">
                                                                0
                                                            </strong>
                                                            <span>Job offers</span>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                            <div className="col-md-4 d-flex justify-content-center counter-wrap ftco-animate">
                                                <div className="block-18 text-center">
                                                    <div className="text d-flex">
                                                        <div className="icon mr-2">
                                                            <span className="flaticon-visitor"></span>
                                                        </div>
                                                        <div className="desc text-left">
                                                            <strong className="numberAnimated" data-number="16">
                                                                0
                                                            </strong>
                                                            <span>Companies</span>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                            <div className="col-md-4 d-flex justify-content-center counter-wrap ftco-animate">
                                                <div className="block-18 text-center">
                                                    <div className="text d-flex">
                                                        <div className="icon mr-2">
                                                            <span className="flaticon-resume"></span>
                                                        </div>
                                                        <div className="desc text-left">
                                                            <strong className="numberAnimated" data-number="20">
                                                                0
                                                            </strong>
                                                            <span>Active Employees</span>
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
                </div>
            </section>

            <div className="section"></div>

            <section className="about-us section">
                <div className="container">
                    <div className="row align-items-center justify-content-center">
                        <div className="col-lg-6 col-md-10 col-12">
                            <div className="content-left wow fadeInLeft" data-wow-delay=".3s">
                                <div calss="row">
                                    <div calss="col-lg-6 col-12">
                                        <div className="row">
                                            <div className="col-lg-6 col-md-6 col-6">
                                                <img className="single-img" src="/images/about/small1.jpg" alt="#" />
                                            </div>
                                            <div className="col-lg-6 col-md-6 col-6">
                                                <img className="single-img mt-50" src="/images/about/small2.jpg" alt="#" />
                                            </div>
                                        </div>
                                    </div>
                                    <div calss="col-lg-6 col-12">
                                        <div className="row">
                                            <div className="col-lg-6 col-md-6 col-6">
                                                <img className="single-img minus-margin" src="/images/about/small3.jpg" alt="#" />
                                            </div>
                                            <div className="col-lg-6 col-md-6 col-6">
                                                <div className="media-body">
                                                    <i className="lni lni-checkmark"></i>
                                                    <h6 className="">Job alert!</h6>
                                                    <p className="">New jobs are available in this week!</p>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div className="col-lg-6 col-md-10 col-12">
                            <div className="content-right wow fadeInRight" data-wow-delay=".5s">
                                <h2>
                                    Help you to get the <br />
                                    best job that fits you
                                </h2>

                                <div className="single-list">
                                    <i className="lni lni-grid-alt"></i>

                                    <div className="list-bod">
                                        <h5>#1 Jobs site in BULGARIA</h5>
                                        <p>Leverage agile frameworks to provide a robust synopsis for high level overviews. Iterative</p>
                                    </div>
                                </div>

                                <div className="single-list">
                                    <i className="lni lni-search"></i>

                                    <div className="list-bod">
                                        <h5>Seamless searching</h5>
                                        <p>Capitalize on low hanging fruit to identify a ballpark value added activity to beta test.</p>
                                    </div>
                                </div>

                                <div className="single-list">
                                    <i className="lni lni-stats-up"></i>

                                    <div className="list-bod">
                                        <h5>Hired in top companies</h5>
                                        <p>Podcasting operational change management inside of workflows to establish.</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <section className="call-action overlay section">
                <div className="container">
                    <div className="row ">
                        <div className="col-lg-8 offset-lg-2 col-12">
                            <div className="inner">
                                <div className="section-title">
                                    <span className="wow fadeInDown" data-wow-delay=".2s">
                                        GETTING STARTED TO WORK
                                    </span>
                                    <h2 className="wow fadeInUp" data-wow-delay=".4s">
                                        Don’t just find. Be found. Put your CV in front of great employers
                                    </h2>
                                    <p className="wow fadeInUp" data-wow-delay=".6s">
                                        It helps you to increase your chances of finding a suitable job and let recruiters contact you about jobs that are not needed to pay for advertising.
                                    </p>
                                    <div className="button wow fadeInUp" data-wow-delay=".8s">
                                        <a href="#" className="btn">
                                            <i className="lni lni-upload"></i> Make Your Resume
                                        </a>
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
