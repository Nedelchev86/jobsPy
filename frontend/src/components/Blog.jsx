const Blog = () => {
    return (
        <>
            <div className="breadcrumbs overlay">
                <div className="container">
                    <div className="row">
                        <div className="col-12">
                            <div className="breadcrumbs-content">
                                <h1 className="page-title">News and blogs / Django Rest Framework</h1>
                                <p>
                                    First steps in Django Rest Framework
                                    <br />{" "}
                                </p>
                            </div>
                            <ul className="breadcrumb-nav">
                                <li>
                                    <a href="#">Home</a>
                                </li>
                                <li>Blogs</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>

            <section className="section latest-news-area blog-list">
                <div className="container">
                    <div className="row">
                        <div className="col-lg-8 col-md-7 col-12">
                            <div id="blog-list" className="row"></div>

                            <div className="pagination center">
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
                            </div>
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
