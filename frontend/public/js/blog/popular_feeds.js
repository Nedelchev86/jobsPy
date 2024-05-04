document.addEventListener('DOMContentLoaded', function() {
    // Make an AJAX request to fetch the latest 5 blog posts
    fetch('/api/blog/last/')
        .then(response => response.json())
        .then(data => {
            // Update HTML content with the retrieved data
            const popularFeeds = document.querySelector('.popular-feed-loop');
            data.forEach(blog => {
                const feed = document.createElement('div');
                feed.classList.add('single-popular-feed');
                feed.innerHTML = `
                    <div class="feed-desc">
                        <h6 class="post-title"><a href="/blog/${blog.id}/">${blog.title}</a></h6>
                        <span class="time"><i class="lni lni-calendar"></i> ${blog.created_at}</span>
                    </div>
                `;
                popularFeeds.appendChild(feed);
            });
        })
        .catch(error => {
            console.error('Error fetching latest blog posts:', error);
        });
});
