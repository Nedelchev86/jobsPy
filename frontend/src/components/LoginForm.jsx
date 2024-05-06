import React, {useState} from "react";
import Breadcrumbs from "./Breadcrumbs";

const LoginForm = () => {
    const [formData, setFormData] = useState({
        email: "",
        password: "",
    });
    const [error, setError] = useState("");

    const handleChange = (e) => {
        setFormData({...formData, [e.target.name]: e.target.value});
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await fetch("http://127.0.0.1:8000/api/token/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(formData),
            });

            if (!response.ok) {
                throw new Error("Invalid email or password");
            }

            const data = await response.json();
            localStorage.setItem("token", data.access); // Store token in local storage
            window.location.href = "/";
        } catch (error) {
            console.error("Login failed:", error.message);
            setError(error.message);
        }
    };

    return (
        <>
            <Breadcrumbs pageTitle="Login" pageInfo="Login to your account" />
            <form onSubmit={handleSubmit}>
                {error && <div className="error-message">{error}</div>}
                <div>
                    <label>Email:</label>
                    <input type="email" name="email" value={formData.email} onChange={handleChange} required />
                </div>
                <div>
                    <label>Password:</label>
                    <input type="password" name="password" value={formData.password} onChange={handleChange} required />
                </div>
                <button type="submit">Login</button>
            </form>
        </>
    );
};

export default LoginForm;
