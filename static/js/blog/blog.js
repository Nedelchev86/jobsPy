//document.addEventListener('DOMContentLoaded', function() {
//    fetch('`/api/blog/?page=${page}&page_size=${pageSize}')
//        .then(response => response.json())
//        .then(data => {
//        console.log(data.results)
//
//            const blogList = document.getElementById('blog-list');
//            data.forEach(blog => {
//                const div = document.createElement('div');
//                div.classList.add('col-lg-6', 'col-12');
//                div.innerHTML = `
//                    <div class="single-news wow">
//                        <div class="image">
//                            <img class="thumb" src="${blog.image_url_1}" alt="#">
//                        </div>
//                        <div class="content-body">
//                            <h4 class="title"><a href="blog-single.html">${blog.title}</a></h4>
//                            <div class="meta-details">
//                                <ul>
//                                    <li><a href="#"><i class="lni lni-tag"></i> ${blog.author.first_name} ${blog.author.last_name}</a></li>
//                                    <li><a href="#"><i class="lni lni-calendar"></i> ${blog.created_at.split("T")[0]}</a></li>
//                                    <li><a href="#"><i class="lni lni-eye"></i>${blog.views}</a></li>
//                                </ul>
//                            </div>
//                            <div class="truncate-overflow">
//                            <p>${blog.description}</p>
//                            <div>
//                            <div class="button">
//                                <a href="/blog/${blog.id}/" class="btn">Read More</a>
//                            </div>
//                        </div>
//                    </div>`;
//                blogList.appendChild(div);
//            });
//        })
//        .catch(error => {
//            console.error('Error fetching blogs:', error);
//        });
//});



document.addEventListener('DOMContentLoaded', function() {
    // Define function to create pagination links
    function createPaginationLinks(count, currentPage, pageSize) {
        const paginationDiv = document.createElement('div');
        paginationDiv.classList.add('pagination', 'center');
        const paginationList = document.createElement('ul');
        paginationList.classList.add('pagination-list');

        // Calculate total number of pages
        const totalPages = Math.ceil(count / pageSize);

        // Create "Previous" button
        const prevPageLi = document.createElement('li');
        const prevPageLink = document.createElement('a');
        prevPageLink.href = '#';
        prevPageLink.innerHTML = '<i class="lni lni-chevron-left"></i>';
        prevPageLink.addEventListener('click', function(event) {
            event.preventDefault();
            if (currentPage > 1) {
                fetchBlogs(currentPage - 1, pageSize);
            }
        });
        prevPageLi.appendChild(prevPageLink);
        paginationList.appendChild(prevPageLi);

        // Create page number links
        for (let i = 1; i <= totalPages; i++) {
            const pageLi = document.createElement('li');
            const pageLink = document.createElement('a');
            pageLink.href = '#';
            pageLink.textContent = i;
            if (i === currentPage) {
                pageLi.classList.add('active');
            }
            pageLink.addEventListener('click', function(event) {
                event.preventDefault();
                fetchBlogs(i, pageSize);
            });
            pageLi.appendChild(pageLink);
            paginationList.appendChild(pageLi);
        }

        // Create "Next" button
        const nextPageLi = document.createElement('li');
        const nextPageLink = document.createElement('a');
        nextPageLink.href = '#';
        nextPageLink.innerHTML = '<i class="lni lni-chevron-right"></i>';
        nextPageLink.addEventListener('click', function(event) {
            event.preventDefault();
            if (currentPage < totalPages) {
                fetchBlogs(currentPage + 1, pageSize);
            }
        });
        nextPageLi.appendChild(nextPageLink);
        paginationList.appendChild(nextPageLi);

        paginationDiv.appendChild(paginationList);
        return paginationDiv;
    }


    // Define a function to fetch blogs with pagination
    function fetchBlogs(page = 1, pageSize = 10) {
        fetch(`/api/blog/?page=${page}&page_size=${pageSize}`)
            .then(response => response.json())
            .then(data => {
                // Clear existing blog list content
                const blogList = document.getElementById('blog-list');
                blogList.innerHTML = '';

                // Iterate over fetched blogs and append them to the blog list
                data.results.forEach(blog => {
                    const div = document.createElement('div');
                    div.classList.add('col-lg-6', 'col-12');
                    div.innerHTML = `
                        <div class="single-news wow">
                            <div class="image">
                                <img class="thumb" src="${blog.image_url_1}" alt="#">
                            </div>
                            <div class="content-body">
                                <h4 class="title"><a href="blog-single.html">${blog.title}</a></h4>
                                <div class="meta-details">
                                    <ul>
                                        <li><a href="#"><i class="lni lni-tag"></i> ${blog.author.first_name} ${blog.author.last_name}</a></li>
                                        <li><a href="#"><i class="lni lni-calendar"></i> ${blog.created_at.split("T")[0]}</a></li>
                                        <li><a href="#"><i class="lni lni-eye"></i>${blog.views}</a></li>
                                    </ul>
                                </div>
                                <div class="truncate-overflow">
                                    <p>${blog.description}</p>
                                </div>
                                <div class="button">
                                    <a href="/blog/${blog.id}/" class="btn">Read More</a>
                                </div>
                            </div>
                        </div>`;
                    blogList.appendChild(div);

                });

                const pagination = createPaginationLinks(data.count, page, pageSize);
                console.log(pagination)
                const paginationDiv = document.getElementsByClassName("pagination")[0]
                paginationDiv.innerHTML = ""
                paginationDiv.appendChild(pagination);

                // Optionally, you can also handle pagination controls here
                // For example, creating "Previous" and "Next" buttons based on the 'next' and 'previous' links in the response.
            })
            .catch(error => {
                console.error('Error fetching blogs:', error);
            });
    }

    // Fetch blogs when the DOM content is loaded
    fetchBlogs();
});
