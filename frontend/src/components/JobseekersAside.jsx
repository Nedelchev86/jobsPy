import React, {useState} from "react";

export default function JobSeekersAside({onSearch}) {
    const [city, setCity] = useState("");

    const handleSubmit = (event) => {
        event.preventDefault();
        onSearch(city); // Call the parent component's onSearch function with the city
    };

    const handleChange = (event) => {
        setCity(event.target.value);
    };

    return (
        <aside className="col-lg-4 col-md-12 col-12">
            <div className="sidebar">
                <div className="widget search-widget">
                    <form onSubmit={handleSubmit}>
                        <input type="text" name="city" placeholder="Search by city..." value={city} onChange={handleChange} />
                        <button type="submit">
                            <i className="lni lni-search-alt"></i>
                        </button>
                    </form>
                </div>
                {/* Other widgets */}
            </div>
        </aside>
    );
}
