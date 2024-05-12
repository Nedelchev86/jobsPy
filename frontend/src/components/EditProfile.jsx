// import JobSeekerMenu from "./JobseekerMenu";
// import Breadcrumbs from "./Breadcrumbs";
// import {useState, useEffect} from "react";
// import {useAuth} from "../contexts/Contexts";

// export default function EditProfile() {
//     const {auth, isAuthenticated} = useAuth();
//     console.log(auth);

//     if (!isAuthenticated) {
//         return <div>Not authenticated...</div>;
//     }

//     const [formData, setFormData] = useState({
//         first_name: "",
//         last_name: "",
//         city: "",
//         nationality: "",
//         occupation: "",
//         seniority: null, // Assuming seniority is a foreign key, initialize to null
//         website: "",
//         linkedin: "",
//         facebook: "",
//         github: "",
//         about: "",
//         phone_number: "",
//         gender: "", // Assuming gender is a string, initialize to an empty string
//         marital_status: "", // Assuming marital_status is a string, initialize to an empty string
//         skills: [], // Assuming skills is an array, initialize to an empty array
//         profile_picture: null, // For file upload, initialize to null
//     });

//     useEffect(() => {
//         if (!formData) {
//             console.log("loading");
//             return <div>Loading</div>;
//         }

//         // Fetch user's profile data from the backend
//         fetch("http://127.0.0.1:8000/api/user/jobseeker/update/", {
//             method: "GET",
//             headers: {
//                 "Content-Type": "application/json",
//                 Authorization: `Bearer ${auth}`,
//             },
//         })
//             .then((response) => response.json())
//             .then((data) => setFormData(data))

//             .catch((error) => {
//                 console.error("Error fetching profile data:", error);
//             });
//     }, []); // Run this effect only once when component mounts

//     console.log(formData);
//     const handleChange = (e) => {
//         const {name, value} = e.target;
//         setFormData((prevState) => ({
//             ...prevState,
//             [name]: value,
//         }));
//     };

//     // const handleFileChange = (e) => {
//     //     const file = e.target.files[0];
//     //     setFormData((prevState) => ({
//     //         ...prevState,
//     //         profile_picture: file,
//     //     }));
//     // };

//     // Function to handle form submission
//     const handleSubmit = (e) => {
//         e.preventDefault();
//         // Submit formData to backend for updating the profile
//         fetch("http://127.0.0.1:8000/api/user/jobseeker/update/", {
//             method: "PUT",
//             headers: {
//                 "Content-Type": "application/json",
//                 Authorization: `Bearer ${auth}`,
//             },
//             body: JSON.stringify(formData),
//         })
//             .then((response) => response.json())
//             .then((data) => {
//                 console.log("Profile updated successfully:", data);
//                 // success response
//             })
//             .catch((error) => {
//                 console.error("Error updating profile:", error);
//                 // error
//             });
//     };

//     return (
//         <>
//             <Breadcrumbs pageTitle="Edit Profile" pageInfo="Edit Profile" />
//             <div className="change-password section">
//                 <div className="container">
//                     <div className="alerts-inner">
//                         <div className="row">
//                             <JobSeekerMenu />

//                             <div className="col-lg-8">
//                                 <div className="password-content">
//                                     <h3>Edit Profile</h3>
//                                     <p>Here you can edit your Profile.</p>
//                                     <form onSubmit={handleSubmit} encType="multipart/form-data">
//                                         <input type="text" name="first_name" value={formData.first_name} onChange={handleChange} />
//                                         <input type="text" name="last_name" value={formData.last_name} onChange={handleChange} />
//                                         <input type="text" name="city" value={formData.city} onChange={handleChange} />
//                                         <input type="text" name="nationality" value={formData.nationality} onChange={handleChange} />
//                                         <input type="text" name="occupation" value={formData.occupation} onChange={handleChange} />
//                                         {/* <select name="seniority" value={formData.seniority} onChange={handleChange}>

//                                         </select> */}
//                                         <input type="url" name="website" value={formData.website} onChange={handleChange} />
//                                         <input type="url" name="linkedin" value={formData.linkedin} onChange={handleChange} />
//                                         <input type="url" name="facebook" value={formData.facebook} onChange={handleChange} />
//                                         <input type="url" name="github" value={formData.github} onChange={handleChange} />
//                                         <textarea name="about" value={formData.about} onChange={handleChange}></textarea>
//                                         <input type="text" name="phone_number" value={formData.phone_number} onChange={handleChange} />
//                                         {/* <input type="file" name="profile_picture" onChange={handleFileChange} /> */}
//                                         {/* <select name="gender" value={formData.gender} onChange={handleChange}>

//                                         </select> */}
//                                         {/* <select name="marital_status" value={formData.marital_status} onChange={handleChange}>

//                                         </select> */}
//                                         <div>{/* Render checkboxes for skills */}</div>
//                                         <button type="submit">Save</button>
//                                     </form>
//                                     {/* {% if form.errors %}
//                             <div className="alert alert-danger">
//                             {{ form.errors }}
//                             </div>
//                             {% endif %} */}

//                                     <form method="post">
//                                         <div className="row">
//                                             {/* {{ form.media }} */}
//                                             {/* {% for field in form %}
//                     <div className="form-group">
//                     {{ field.label_tag }}
//                     {{ field }}
//                      </div>
//                     {% for error in field.errors %}
//                       <p style="color: red">{{ error }}</p>
//                     {% endfor %}

//                 {% endfor %} */}

//                                             <div className="col-lg-12">
//                                                 <div className="button">
//                                                     <button className="btn">Save</button>
//                                                 </div>
//                                             </div>
//                                         </div>
//                                     </form>
//                                 </div>
//                             </div>
//                         </div>
//                     </div>
//                 </div>
//             </div>
//         </>
//     );
// }

import JobSeekerMenu from "./JobseekerMenu";
import Breadcrumbs from "./Breadcrumbs";
import {useState, useEffect} from "react";
import {useAuth} from "../contexts/Contexts";

export default function EditProfile() {
    const {auth, isAuthenticated} = useAuth();
    const [profile, setProfile] = useState({
        first_name: "",
        last_name: "",
        city: "",
        nationality: "",
        occupation: "",
        website: "",
        linkedin: "",
        facebook: "",
        github: "",
        about: "",
        phone_number: "",
        gender: "",
        marital_status: "",
        skills: [], // Assume skills are selected by default
    });

    if (!isAuthenticated) {
        return <div>Not authenticated...</div>;
    }

    useEffect(() => {
        // Fetch user's profile data from the backend
        fetch("http://127.0.0.1:8000/api/user/jobseeker/update/", {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
                Authorization: `Bearer ${auth}`,
            },
        })
            .then((response) => response.json())
            .then((data) => setProfile(data))

            .catch((error) => {
                console.error("Error fetching profile data:", error);
            });
    }, [auth]); // Run this effect only once when component mounts

    const handleChange = (e) => {
        const {name, value} = e.target;
        setProfile((prevState) => ({
            ...prevState,
            [name]: value,
        }));
    };

    // const handleFileChange = (e) => {
    //     const file = e.target.files[0];
    //     setprofile((prevState) => ({
    //         ...prevState,
    //         profile_picture: file,
    //     }));
    // };

    // Function to handle form submission
    const handleSubmit = (e) => {
        e.preventDefault();
        // Submit profile to backend for updating the profile
        fetch("http://127.0.0.1:8000/api/user/jobseeker/update/", {
            method: "PUT",
            headers: {
                "Content-Type": "application/json",
                Authorization: `Bearer ${auth}`,
            },
            body: JSON.stringify(profile),
        })
            .then((response) => response.json())
            .then((data) => {
                console.log("Profile updated successfully:", data);
                // success response
            })
            .catch((error) => {
                console.error("Error updating profile:", error);
                // error
            });
    };

    return (
        <>
            <Breadcrumbs pageTitle="Edit Profile" pageInfo="Edit Profile" />
            <div className="change-password section">
                <div className="container">
                    <div className="alerts-inner">
                        <div className="row">
                            <JobSeekerMenu />

                            <div className="col-lg-8">
                                <div className="password-content">
                                    <h3>Edit Profile</h3>
                                    <p>Here you can edit your Profile.</p>

                                    <form onSubmit={handleSubmit} encType="multipart/form-data">
                                        <div className="row">
                                            <div className="form-group">
                                                <label htmlFor="id_first_name" className="required">
                                                    First Name:
                                                </label>
                                                <input type="text" name="first_name" value={profile.first_name} maxLength="50" className="form-control" onChange={handleChange} required id="id_first_name" />
                                            </div>

                                            <div className="form-group">
                                                <label htmlFor="id_last_name" className="required">
                                                    Last name:
                                                </label>
                                                <input type="text" name="last_name" value={profile.last_name} maxLength="50" className="form-control" onChange={handleChange} required id="id_last_name" />
                                            </div>

                                            <div className="form-group">
                                                <label htmlFor="id_city" className="required">
                                                    City:
                                                </label>
                                                <input type="text" name="city" value={profile.city} maxLength="50" className="form-control" onChange={handleChange} required id="id_city" />
                                            </div>

                                            <div className="form-group">
                                                <label htmlFor="id_nationality" className="required">
                                                    Nationality:
                                                </label>
                                                <input type="text" name="nationality" value={profile.nationality} maxLength="50" className="form-control" onChange={handleChange} required id="id_nationality" />
                                            </div>

                                            <div className="form-group">
                                                <label htmlFor="id_occupation" className="required">
                                                    Occupation:
                                                </label>
                                                <input type="text" name="occupation" value={profile.occupation} maxLength="50" className="form-control" onChange={handleChange} required id="id_occupation" />
                                            </div>

                                            <div className="form-group">
                                                <label htmlFor="id_seniority">Seniority:</label>
                                                {/* <select name="seniority" className="form-control" id="id_seniority">
                                                    <option value="">---------</option>

                                                    <option value="1">Junior / Intern</option>

                                                    <option value="2">1-2 year&#x27;s experience</option>

                                                    <option value="3">2-5 year&#x27;s experience</option>

                                                    <option value="4" selected>
                                                        5+ year&#x27;s experience
                                                    </option>
                                                </select> */}
                                            </div>

                                            <div className="form-group">
                                                <label htmlFor="id_website">Website:</label>
                                                <input type="url" name="website" value={profile.website} onChange={handleChange} maxLength="70" className="form-control" id="id_website" />
                                            </div>

                                            <div className="form-group">
                                                <label htmlFor="id_linkedin">Linkedin:</label>
                                                <input type="url" value={profile.linkedin} onChange={handleChange} name="linkedin" maxLength="50" className="form-control" id="id_linkedin" />
                                            </div>

                                            <div className="form-group">
                                                <label htmlFor="id_facebook">Facebook:</label>
                                                <input type="url" name="facebook" maxLength="50" value={profile.facebook} onChange={handleChange} className="form-control" id="id_facebook" />
                                            </div>

                                            <div className="form-group">
                                                <label htmlFor="id_github">Github:</label>
                                                <input type="url" name="github" maxLength="50" value={profile.github} onChange={handleChange} className="form-control" id="id_github" />
                                            </div>

                                            <div className="form-group">
                                                <label htmlFor="id_about" className="required">
                                                    About:
                                                </label>
                                                {/* <div className="django-ckeditor-widget" data-field-id="id_about" style="display: inline-block;">
                                                    <textarea
                                                        name="about"
                                                        cols="40"
                                                        rows="10"
                                                        className="form-control"
                                                        required
                                                        id="id_about"
                                                        data-processed="0"
                                                        data-config='{"skin": "moono-lisa", "toolbar_Basic": [["Source", "-", "Bold", "Italic"]], "toolbar_Full": [["Styles", "Format", "Bold", "Italic", "Underline", "Strike", "SpellChecker", "Undo", "Redo"], ["Link", "Unlink", "Anchor"], ["Image", "Flash", "Table", "HorizontalRule"], ["TextColor", "BGColor"], ["Smiley", "SpecialChar"], ["Source"]], "toolbar": "Full", "height": 291, "width": "100%", "filebrowserWindowWidth": 940, "filebrowserWindowHeight": 725, "removePlugins": "exportpdf", "versionCheck": false, "language": "en-us"}'
                                                        data-external-plugin-resources="[]"
                                                        data-id="id_about"
                                                        data-type="ckeditortype"
                                                        value={profile.about}
                                                    >
                                                        &lt;p&gt;fref&lt;/p&gt;
                                                    </textarea>
                                                </div> */}
                                            </div>

                                            {/* <div className="form-group">
                                                <label htmlFor="id_phone_number">Phone number:</label>
                                                <input type="text" name="phone_number" maxLength="50" className="form-control" id="id_phone_number" />
                                            </div>

                                            <div className="form-group">
                                                <label htmlFor="id_profile_picture">Image:</label>
                                                Currently: <a href="https://res.cloudinary.com/drjgddl0y/image/upload/v1713289021/qqxwvsy7ptxswlpeiih1.jpg">qqxwvsy7ptxswlpeiih1</a>
                                                <input type="checkbox" name="profile_picture-clear" id="profile_picture-clear_id" />
                                                <label htmlFor="profile_picture-clear_id">Clear</label>
                                                <br />
                                                Change:
                                                <input type="file" name="profile_picture" className="form-control" id="id_profile_picture" />
                                            </div> */}

                                            <div className="form-group">
                                                <label htmlFor="id_gender" className="required">
                                                    Gender:
                                                </label>
                                                {/* <select name="gender" className="form-control" onChange={handleChange} required id="id_gender">
                                                    <option value="">---------</option>

                                                    <option value="M" selected>
                                                        Male
                                                    </option>

                                                    <option value="F">Female</option>
                                                </select>*/}
                                            </div>

                                            <div className="form-group">
                                                <label htmlFor="id_marital_status">Marital status:</label>
                                                {/* <select name="marital_status" className="form-control" id="id_marital_status">
                                                    <option value="" selected>
                                                        ---------
                                                    </option>

                                                    <option value="Married">Married</option>

                                                    <option value="Unmarried">Unmarried</option>

                                                    <option value="Devorced">Devorced</option>
                                                </select> */}
                                            </div>

                                            {/* <div className="form-group">
                                                <label>Skills:</label>
                                                <div id="id_skills" className="form-check">
                                                    <div>
                                                        <label htmlFor="id_skills_0">
                                                            <input type="checkbox" name="skills" value="1" className="form-check" id="id_skills_0" checked />
                                                            Python
                                                        </label>
                                                    </div>
                                                    <div>
                                                        <label htmlFor="id_skills_1">
                                                            <input type="checkbox" name="skills" value="2" className="form-check" id="id_skills_1" checked />
                                                            Java
                                                        </label>
                                                    </div>
                                                    <div>
                                                        <label htmlFor="id_skills_2">
                                                            <input type="checkbox" name="skills" value="3" className="form-check" id="id_skills_2" />
                                                            Django
                                                        </label>
                                                    </div>
                                                    <div>
                                                        <label htmlFor="id_skills_3">
                                                            <input type="checkbox" name="skills" value="4" className="form-check" id="id_skills_3" />
                                                            Docker
                                                        </label>
                                                    </div>
                                                    <div>
                                                        <label htmlFor="id_skills_4">
                                                            <input type="checkbox" name="skills" value="5" className="form-check" id="id_skills_4" />
                                                            PostgreSQL
                                                        </label>
                                                    </div>
                                                    <div>
                                                        <label htmlFor="id_skills_5">
                                                            <input type="checkbox" name="skills" value="6" className="form-check" id="id_skills_5" />
                                                            C++
                                                        </label>
                                                    </div>
                                                    <div>
                                                        <label htmlFor="id_skills_6">
                                                            <input type="checkbox" name="skills" value="7" className="form-check" id="id_skills_6" />
                                                            JavaScript
                                                        </label>
                                                    </div>
                                                    <div>
                                                        <label htmlFor="id_skills_7">
                                                            <input type="checkbox" name="skills" value="8" className="form-check" id="id_skills_7" checked />
                                                            React
                                                        </label>
                                                    </div>
                                                    <div>
                                                        <label htmlFor="id_skills_8">
                                                            <input type="checkbox" name="skills" value="9" className="form-check" id="id_skills_8" checked />
                                                            Angular
                                                        </label>
                                                    </div>
                                                    <div>
                                                        <label htmlFor="id_skills_9">
                                                            <input type="checkbox" name="skills" value="10" className="form-check" id="id_skills_9" />
                                                            DevOps
                                                        </label>
                                                    </div>
                                                </div>
                                            </div> */}

                                            <div className="col-lg-12">
                                                <div className="button">
                                                    <button className="btn">Save</button>
                                                </div>
                                            </div>
                                        </div>
                                    </form>

                                    {/* {% if form.errors %}
                            <div className="alert alert-danger">
                            {{ form.errors }}
                            </div>
                            {% endif %} */}

                                    <form method="post">
                                        <div className="row">
                                            {/* {{ form.media }} */}
                                            {/* {% for field in form %}
                    <div className="form-group">
                    {{ field.label_tag }}
                    {{ field }}
                     </div>
                    {% for error in field.errors %}
                      <p style="color: red">{{ error }}</p>
                    {% endfor %}

                {% endfor %} */}

                                            <div className="col-lg-12">
                                                <div className="button">
                                                    <button className="btn">Save</button>
                                                </div>
                                            </div>
                                        </div>
                                    </form>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </>
    );
}
