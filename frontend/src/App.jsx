import {react} from "react";
import {BrowserRouter as Router, Routes, Route, Link} from "react-router-dom";
import Header from "./components/Header";
import Footer from "./components/Footer";
import Index from "./components/Index";
import Blog from "./components/Blog";

function App() {
    return (
        <Router>
            <Header />
            <Routes>
                <Route path="/" element={<Index />} />
                <Route path="/blog" element={<Blog />} />
            </Routes>
            <Footer />
        </Router>
    );
}

export default App;
