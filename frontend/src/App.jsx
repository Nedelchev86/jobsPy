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
import JobDetails from "./components/JobDetails";
import JobsFavoriteList from "./components/JobsFavoriteList";
import Breadcrumbs from "./components/Breadcrumbs";
import JobSeekerDashboard from "./components/JobSeekerDashboard";
import JobSeekerLayout from "./components/JobSeekerLayout";
import EditProfile from "./components/EditProfile";
import CreateJob from "./components/CreateJob";
import ApplicantsList from "./components/ApplicantsList";
import CreatedJobs from "./components/CreatedJobs";
import ChangePassword from "./components/ChangePassword";
import CompanyNotifications from "./components/CompanyNotifications";
import ApplicantsForJob from "./components/ApplicantsForJob";
import EditJob from "./components/EditJob";

function App() {
    return (
        <AuthProvider>
            <Header />
            <Routes>
                <Route path="/" element={<Index />} />
                <Route path="blog" element={<Blog />} />
                {/* <Route path="companies" element={<CompanyList />} /> */}
                <Route path="companies">
                    <Route index element={<CompanyList />} />
                    <Route path=":id" element={<CompanyDetails />} />
                </Route>
                <Route path="companies/:id" element={<CompanyDetails />} />
                <Route path="jobseekers" element={<JobseekersList />} />
                <Route path="jobseekers/:id" element={<JobSeekerDetails />} />
                <Route path="jobs" element={<JobsList />} />
                <Route path="signup" element={<RegisterForm />} />
                <Route path="login" element={<LoginForm />} />
                {/* <Route path="dashboard" element={<Dashboard />} /> */}
                {/* <Route path="/bookmarked" element={<JobsFavoriteList />} /> */}
                {/* <Route path="/profile/edit" element={<EditProfile />} /> */}
                <Route path="jobs/:id" element={<JobDetails />} />
                <Route path="dashboard" element={<JobSeekerLayout />}>
                    <Route index element={<Dashboard />} />
                    <Route path="edit" element={<EditProfile />} />
                    <Route path="bookmarked" element={<JobsFavoriteList />} />
                    <Route path="create-job" element={<CreateJob />} />
                    <Route path="edit-job/:id" element={<EditJob />} />
                    <Route path="applicants" element={<ApplicantsList />} />
                    <Route path="applicants/jobs/:id" element={<ApplicantsForJob />} />
                    <Route path="created-jobs" element={<CreatedJobs />} />
                    <Route path="notifications" element={<CompanyNotifications />} />
                    <Route path="change-password" element={<ChangePassword />} />
                </Route>
            </Routes>
            <Footer />
        </AuthProvider>
    );
}

export default App;
