document.addEventListener('DOMContentLoaded', function() {
    // Extract blog ID from URL

    const urlParts = window.location.pathname.split('/');
    const blogId = urlParts[urlParts.length - 2];  // Assuming the ID is the second-to-last part of the URL

    // Make API call to fetch blog post details
    fetch(`/api/blog/${blogId}/`)
        .then(response => response.json())
        .then(blog => {

       const post = document.getElementById("single-post")
        post.innerHTML = `<div class="post-thumbnils">
                            <img id="main-image" src=${blog.image_url_1} alt="#">
                        </div>
                        <div class="post-details">
                            <div class="detail-inner">
                                <h2 class="post-title">
                                    <a href="blog-single.html">${blog.title}</a>
                                </h2>
                                <!-- post meta -->
                                <ul class="custom-flex post-meta">
                                    <li>
                                        <a href="#">
                                            <i class="lni lni-calendar"></i>
                                            ${blog.created_at.split("T")[0]}
                                        </a>
                                    </li>
                                    <li>
                                        <a href="#">
                                            <i class="lni lni-comments"></i>
                                            35 Comments
                                        </a>
                                    </li>
                                    <li>
                                        <a id="views" href="#">
                                            <i class="lni lni-eye"></i>
                                            ${blog.views} View
                                        </a>
                                    </li>
                                </ul>
                                <p>${blog.description}</p>
                                <!-- post image -->
                                <div class="post-image">
                                    <div class="row">

                                        <div class="col-lg-6 col-md-6 col-12">
                                            <a href="#" class="mb-4">

                                                <img id="second-image" src=${blog.image_url_2} alt="#">

                                            </a>
                                        </div>


                                        <div class="col-lg-6 col-md-6 col-12">
                                            <a href="#">

                                                <img src=${blog.image_url_3} alt="#">
                                     </a>
                                        </div>

                                    </div>
                                </div>

                                <p>${blog.more_info}</p>
                                <!-- post quote -->
                                <blockquote>
                                    <div class="icon">
                                        <i class="lni lni-quotation"></i>
                                    </div>
                                    <p>${blog.footer}</p>


                                </blockquote>

                            </div>
        `


        })
        .catch(error => {
            console.error('Error fetching blog post:', error);
        });
});
