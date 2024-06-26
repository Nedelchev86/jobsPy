import {useState, useEffect} from "react";
import Breadcrumbs from "./Breadcrumbs";
import {Link} from "react-router-dom";

export default function CompanyList() {
    const [companies, setCompanies] = useState([]);
    useEffect(() => {
        fetch("http://127.0.0.1:8000/company/api/companies/")
            .then((response) => response.json())
            .then((data) => setCompanies(data));
    }, []);

    return (
        <>
            <Breadcrumbs pageTitle="Companies" pageInfo="Take a look at the top IT companies ..." />

            <section className="job-category style2 section">
                <div className="container">
                    <div className="row">
                        <div className="col-12">
                            <div className="section-title">
                                <span className="wow">Companies</span>
                                <h2 className="wow">Browse by Company</h2>
                                <p className="wow">List of the largest software companies</p>
                            </div>
                        </div>
                    </div>
                    <div className="cat-head">
                        <div className="row">
                            {companies.map((company) => (
                                <div key={company.user} className="col-lg-3 col-md-6 col-12">
                                    <Link to={`/companies/${company.user}`} className="single-cat wow">
                                        <div className="top-side">
                                            <img src={`https://res.cloudinary.com/drjgddl0y/${company.image}`} alt={company.name} />
                                        </div>

                                        <div className="bottom-side">
                                            <span className="available-job2">Jobs</span>
                                            {/* <span className="available-job">{company.user.job_set.all | length}</span> */}
                                            <h3>{company.name}</h3>
                                        </div>
                                    </Link>
                                </div>
                            ))}
                        </div>
                    </div>
                </div>
            </section>
        </>
    );
}
