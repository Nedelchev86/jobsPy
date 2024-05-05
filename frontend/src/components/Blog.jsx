import React, {useState, useEffect} from "react";
import Breadcrumbs from "./Breadcrumbs";

const Blog = () => {
    const [blogs, setBlogs] = useState([]);

    useEffect(() => {
        // Fetch blogs from your API
        fetch("http://127.0.0.1:8000/api/blog/")
            .then((response) => response.json())
            .then((data) => setBlogs(data.results))
            .catch((error) => console.error("Error fetching blogs:", error));
    }, []);

    return (
        <>
            <Breadcrumbs pageTitle="News and blogs / Django Rest Framework" pageInfo="First steps in Django Rest Framework" />

            <section className="section latest-news-area blog-list">
                <div className="container">
                    <div className="row">
                        <div className="col-lg-8 col-md-7 col-12">
                            <div id="blog-list" className="row">
                                {blogs.map((blog) => (
                                    <div className="col-lg-6 col-12" key={blog.id}>
                                        <div className="single-news wow">
                                            <div className="image">
                                                <img className="thumb" src={blog.image_url_1} alt="#" />
                                            </div>
                                            <div className="content-body">
                                                <h4 className="title">
                                                    <a href="/blog/${blog.id}/">{blog.title}</a>
                                                </h4>
                                                <div className="meta-details">
                                                    <ul>
                                                        <li>
                                                            <a href="#">
                                                                <i className="lni lni-tag"></i> {blog.author.first_name} {blog.author.last_name}
                                                            </a>
                                                        </li>
                                                        <li>
                                                            <a href="#">
                                                                <i className="lni lni-calendar"></i> {blog.created_at.split("T")[0]}
                                                            </a>
                                                        </li>
                                                        <li>
                                                            <a href="#">
                                                                <i className="lni lni-eye"></i>
                                                                {blog.views}
                                                            </a>
                                                        </li>
                                                    </ul>
                                                </div>
                                                <div className="truncate-overflow">
                                                    <p>{blog.description}</p>
                                                </div>
                                                <div className="button">
                                                    <a href="/blog/${blog.id}/" className="btn">
                                                        Read More
                                                    </a>
                                                </div>
                                            </div>
                                        </div>
                                        `;
                                    </div>
                                ))}
                            </div>

                            {/* <div className="pagination center">
                                <ul className="pagination-list">
                                    <li>
                                        <a href="#">
                                            <i className="lni lni-chevron-left"></i>
                                        </a>
                                    </li>
                                    <li className="active">
                                        <a href="#">1</a>
                                    </li>
                                    <li>
                                        <a href="#">2</a>
                                    </li>
                                    <li>
                                        <a href="#">3</a>
                                    </li>
                                    <li>
                                        <a href="#">4</a>
                                    </li>
                                    <li>
                                        <a href="#">
                                            <i className="lni lni-chevron-right"></i>
                                        </a>
                                    </li>
                                </ul>
                            </div> */}
                        </div>
                        <aside className="col-lg-4 col-md-5 col-12">
                            <div className="sidebar">
                                {/*                     
                                  {% if 'blog.add_blogpost' in perms %}
                                <div className="sidebar-widget">
                                <div className="inner">
                            <div className="row m-n2 button">
                                        <div className=" col-lg-12  ">
                                            <a href="{% url 'blog-create' %}" className="d-block btn"><i className="fa fa-heart-o mr-1"></i> Add Blog Post</a>
                                        </div>
                                     </div>
                                </div>
                            </div>

                    {% endif %} */}
                                <div className="widget search-widget">
                                    <h5 className="widget-title">
                                        <span>Search ...</span>
                                    </h5>
                                    <form action="#">
                                        <input type="text" placeholder="Search Here..." />
                                        <button type="submit">
                                            <i className="lni lni-search-alt"></i>
                                        </button>
                                    </form>
                                </div>
                                <div className="widget popular-feeds">
                                    <h5 className="widget-title">
                                        <span>Popular Feeds</span>
                                    </h5>
                                </div>
                                <div className="widget categories-widget">
                                    <h5 className="widget-title">
                                        <span>Categories</span>
                                    </h5>
                                </div>
                                <div className="widget popular-tag-widget">
                                    <h5 className="widget-title">
                                        <span>Popular Tags</span>
                                    </h5>
                                </div>
                            </div>
                        </aside>
                    </div>
                </div>
            </section>
        </>
    );
};

export default Blog;
