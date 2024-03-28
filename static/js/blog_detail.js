document.addEventListener('DOMContentLoaded', function() {
    // Extract blog ID from URL

    const urlParts = window.location.pathname.split('/');
    const blogId = urlParts[urlParts.length - 2];  // Assuming the ID is the second-to-last part of the URL

    // Make API call to fetch blog post details
    fetch(`/api/blog/${blogId}/`)
        .then(response => response.json())
        .then(blog => {
            const mainImage = document.getElementById('main-image')
            mainImage.src = blog.image_url_1
            const secondImage = document.getElementById('second-image')
            secondImage.src = blog.image_url_2
            const views = document.getElementById('views')
            views.innerHTML = `<i class="lni lni-eye"></i>${blog.views} View`
            // Render blog post details on the webpage
//            const blogDetails = document.getElementById('blog-details');
//            blogDetails.innerHTML = `
//                <h1>${blog.title}</h1>
//                <p>${blog.description}</p>
//                <!-- Other blog post details -->
//            `;
        })
        .catch(error => {
            console.error('Error fetching blog post:', error);
        });
});
