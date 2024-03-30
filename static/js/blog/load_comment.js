document.addEventListener('DOMContentLoaded', function() {
    // Get the blog post ID from the URL

    const blogPostId = window.location.pathname.split('/')[2]


    // Fetch comments for the current blog post
    fetch(`/api/blog/${blogPostId}/comments/`)
        .then(response => response.json())
        .then(data => {

            // Update HTML with comments
            var commentsList = document.getElementById('comments-list');
            data.forEach(comment => {
                var commentElement = document.createElement('li');

                let name =  "Anonymous"
                if (comment.author.first_name){
                    name = comment.author.first_name}
                else if(comment.author.title){
                     name = comment.author.title
                          }
                let image = "/static/images/clients/default_profile.png"
                if (comment.author.profile_picture){
                    image = comment.author.profile_picture}
                 else if (comment.author.image){
                    image = comment.author.image}



                commentElement.innerHTML  = `
                                                        <div class="comment-img">
                                            <img src=${image} class="rounded-circle" alt="img">
                                        </div>
                                        <div class="comment-desc">
                                            <div class="desc-top">
                                                <h6>${name}</h6>

                                                <span class="date">${comment.created_at}</span>
                                                <a href="#" class="reply-link"><i class="lni lni-reply"></i>Reply</a>
                                            </div>
                                            <p>
                                               ${comment.content}
                                            </p>
                                        </div>
                `

                commentsList.appendChild(commentElement);
            });
        })
        .catch(error => {
            console.error('Error fetching comments:', error);
        });
});