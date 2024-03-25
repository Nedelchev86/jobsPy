document.addEventListener('DOMContentLoaded', function() {
    console.log("test");
    fetch('/api/blog/')
        .then(response => response.json())
        .then(data => {
            const blogList = document.getElementById('blog-list');
            data.forEach(blog => {
                console.log(blog);
                const div = document.createElement('div');
                div.classList.add('col-lg-6', 'col-12');
                div.innerHTML = `
                    <div class="single-news wow fadeInUp" data-wow-delay=".5s">
                        <div class="image">
                            <img class="thumb" src="${blog.image_url_1}" alt="#">
                        </div>
                        <div class="content-body">
                            <h4 class="title"><a href="blog-single.html">${blog.title}</a></h4>
                            <div class="meta-details">
                                <ul>
                                    <li><a href="#"><i class="lni lni-tag"></i> Career advice</a></li>
                                    <li><a href="#"><i class="lni lni-calendar"></i> 10-10-2023</a></li>
                                    <li><a href="#"><i class="lni lni-eye"></i> 55</a></li>
                                </ul>
                            </div>
                            <p>${blog.description}</p>
                            <div class="button">
                                <a href="blog-single.html" class="btn">Read More</a>
                            </div>
                        </div>
                    </div>`;
                blogList.appendChild(div);
            });
        })
        .catch(error => {
            console.error('Error fetching blogs:', error);
        });
});
