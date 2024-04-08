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


//document.addEventListener('DOMContentLoaded', function() {
//    // Extract blog ID from URL
//    const urlParts = window.location.pathname.split('/');
//    const blogId = urlParts[urlParts.length - 2];  // Assuming the ID is the second-to-last part of the URL
//
//    // Make API call to fetch blog post details
//    fetch(`/api/blog/${blogId}/`)
//        .then(response => response.json())
//        .then(blog => {
//
//            const post = document.getElementById("single-post");
//            post.innerHTML = ""
//
//            // Create post thumbnail
//            const postThumbnail = document.createElement('div');
//            postThumbnail.classList.add('post-thumbnils');
//            const mainImage = document.createElement('img');
//            mainImage.id = 'main-image';
//            mainImage.src = blog.image_url_1;
//            mainImage.alt = '#';
//            postThumbnail.appendChild(mainImage);
//
//            // Create post details
//            const postDetails = document.createElement('div');
//            postDetails.classList.add('post-details');
//            const detailInner = document.createElement('div');
//            detailInner.classList.add('detail-inner');
//
//            // Create post title
//            const postTitle = document.createElement('h2');
//            postTitle.classList.add('post-title');
//            const postTitleLink = document.createElement('a');
//            postTitleLink.href = 'blog-single.html';
//            postTitleLink.textContent = blog.title;
//            postTitle.appendChild(postTitleLink);
//
//            // Create post meta
//            const postMeta = document.createElement('ul');
//            postMeta.classList.add('custom-flex', 'post-meta');
//            const metaItems = [
//                { iconClass: ['lni', 'lni-calendar'], text: blog.created_at.split("T")[0] },
//                { iconClass: ['lni', 'lni-comments'], text: '35 Comments' },
//                { iconClass: ['lni', 'lni-eye'], text: `${blog.views} View` }
//            ];
//            metaItems.forEach(item => {
//                const li = document.createElement('li');
//                const link = document.createElement('a');
//                link.href = '#';
//                const icon = document.createElement('i');
//                icon.classList.add(item.iconClass);
//                link.appendChild(icon);
//                link.innerHTML += item.text;
//                li.appendChild(link);
//                postMeta.appendChild(li);
//            });
//
//            // Create post content
//            const postContent = document.createElement('p');
//            postContent.textContent = blog.description;
//
//            // Create post images
//            const postImages = document.createElement('div');
//            postImages.classList.add('post-image');
//            const imagesRow = document.createElement('div');
//            imagesRow.classList.add('row');
//            const imageUrls = [blog.image_url_2, blog.image_url_3];
//            imageUrls.forEach(url => {
//                const col = document.createElement('div');
//                col.classList.add('col-lg-6', 'col-md-6', 'col-12');
//                const imageLink = document.createElement('a');
//                imageLink.href = '#';
//                const image = document.createElement('img');
//                image.src = url;
//                image.alt = '#';
//                imageLink.appendChild(image);
//                col.appendChild(imageLink);
//                imagesRow.appendChild(col);
//            });
//            postImages.appendChild(imagesRow);
//
//            // Create more info content
//            const moreInfo = document.createElement('p');
//            moreInfo.textContent = blog.more_info;
//
//            // Create post quote
//            const postQuote = document.createElement('blockquote');
//            const quoteIcon = document.createElement('div');
//            quoteIcon.classList.add('icon');
//            const quoteIconInner = document.createElement('i');
//            quoteIconInner.classList.add('lni', 'lni-quotation');
//            quoteIcon.appendChild(quoteIconInner);
//            postQuote.appendChild(quoteIcon);
//            const quoteContent = document.createElement('p');
//            quoteContent.textContent = blog.footer;
//            postQuote.appendChild(quoteContent);
//
//            // Append all elements to post details
//            detailInner.appendChild(postTitle);
//            detailInner.appendChild(postMeta);
//            detailInner.appendChild(postContent);
//            detailInner.appendChild(postImages);
//            detailInner.appendChild(moreInfo);
//            detailInner.appendChild(postQuote);
//            postDetails.appendChild(detailInner);
//
//            // Append post thumbnail and details to post element
//            post.appendChild(postThumbnail);
//            post.appendChild(postDetails);
//        })
//        .catch(error => {
//            console.error('Error fetching blog post:', error);
//        });
//});
