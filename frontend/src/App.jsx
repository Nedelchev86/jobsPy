import {react} from "react";
import {BrowserRouter as Router, Routes, Route, Link} from "react-router-dom";
import Header from "./components/Header";
import Footer from "./components/Footer";
import Index from "./components/Index";
import Blog from "./components/Blog";
import CompanyList from "./components/CompanyList";
import JobseekersList from "./components/Jobseekers";
import JobSeekerDetails from "./components/JobSeekerDetails";
import JobsList from "./components/JobsList";
import CompanyDetails from "./components/CompanyDetails";
import RegisterForm from "./components/RegisterForm";
import LoginForm from "./components/LoginForm";
import {AuthProvider} from "./contexts/Contexts"; // Import AuthProvider
import Dashboard from "./components/Dashboard";

function App() {
    return (
        <>
            {" "}
            <AuthProvider>
                <Header />
                <Routes>
                    <Route path="/" element={<Index />} />
                    <Route path="/blog" element={<Blog />} />
                    <Route path="/companies" element={<CompanyList />} />
                    <Route path="/company/:id" element={<CompanyDetails />} />
                    <Route path="/jobseekers" element={<JobseekersList />} />
                    <Route path="/jobseeker/:id" element={<JobSeekerDetails />} />
                    <Route path="/jobs" element={<JobsList />} />
                    <Route path="/signup" element={<RegisterForm />} />
                    <Route path="/login" element={<LoginForm />} />
                    <Route path="*" element={<Dashboard />} />
                </Routes>
                <Footer />
            </AuthProvider>
        </>
    );
}

export default App;
