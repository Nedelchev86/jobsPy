import {Breadcrumb} from "react-bootstrap";
import {Link, NavLink} from "react-router-dom";

export default function JobSeekerMenu() {
    return (
        <div className="col-lg-4 col-12">
            <div className="dashbord-sidebar">
                <ul>
                    <li className="heading">Manage Account</li>
                    <li>
                        <NavLink activeclassname="active" className="" to="/dashboard">
                            <i className="lni lni-clipboard"></i> Dashboard
                        </NavLink>
                    </li>
                    <li>
                        <NavLink activeclassname="active" className="" to="/profile/edit">
                            <i className="lni lni-clipboard"></i> Edit Profile{" "}
                        </NavLink>
                    </li>
                    <li>
                        <NavLink activeclassname="active" className="" to="{% url 'favourite_jobs' %}">
                            <i className="lni lni-clipboard"></i> Bookmarked Jobs <span className="notifi"></span>
                        </NavLink>
                    </li>
                    <li>
                        <NavLink activeclassname="active" className="" to="{% url 'jobs-apply' %}">
                            <i className="lni lni-alarm"></i>Job Applications <span className="notifi"></span>
                        </NavLink>
                    </li>

                    {/* {% if 'main.add_newsletter' in perms %}
                <li><NavLink className="{% if request.resolver_match.url_name == 'newsletter' %}active{% endif %}" to="{% url 'newsletter' %}"><i className="lni lni-alarm"></i>Send Newsletter </NavLink></li>
               {% endif %} */}
                    <li>
                        <NavLink activeclassname="active" to="/">
                            <i className="lni lni-alarm"></i> Notifications <span className="notifi"></span>
                        </NavLink>
                    </li>
                    <li>
                        <NavLink activeclassname="active" className="" to="{% url 'change-password' %}">
                            <i className="lni lni-lock"></i> Change Password
                        </NavLink>
                    </li>
                    <li>
                        <NavLink activeclassname="active" className="" style={{color: "red"}} to="{% url 'delete_profile' %}">
                            <i className="lni lni-lock"></i> Delete Profile
                        </NavLink>
                    </li>
                    <li>
                        <NavLink activeclassname="active" to="/">
                            <i className="lni lni-upload"></i> Sign Out
                        </NavLink>
                    </li>
                </ul>
            </div>
        </div>
    );
}
