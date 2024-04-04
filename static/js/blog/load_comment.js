document.addEventListener('DOMContentLoaded', function() {
    // Get the blog post ID from the URL
    const blogPostId = window.location.pathname.split('/')[2];
    loadComment(blogPostId);
});


function loadComment(blogPostId) {
    fetch(`/api/blog/${blogPostId}/comments/`)
        .then(response => response.json())
        .then(data => {
            const commentNumber = document.getElementById("comment-number");
            commentNumber.textContent = `${data.length}  comments`;

            // Update HTML with comments
            var commentsList = document.getElementById('comments-list');
            data.forEach(comment => {
                var commentElement = document.createElement('li');

                let name = "Anonymous";
                if (comment.author.first_name) {
                    name = comment.author.first_name;
                } else if (comment.author.name) {
                    name = comment.author.name;
                }
                let image = "/static/images/clients/default_profile.png";
                if (comment.author.profile_picture) {
                    image = comment.author.profile_picture;
                } else if (comment.author.image) {
                    image = comment.author.image;
                }

                // Create comment elements
                var commentImg = document.createElement('div');
                commentImg.classList.add('comment-img');
                var img = document.createElement('img');
                img.src = image;
                img.classList.add('rounded-circle');
                img.alt = 'img';
                commentImg.appendChild(img);

                var commentDesc = document.createElement('div');
                commentDesc.classList.add('comment-desc');

                var descTop = document.createElement('div');
                descTop.classList.add('desc-top');
                var h6 = document.createElement('h6');
                h6.textContent = name;
                var span = document.createElement('span');
                span.classList.add('date');
                span.textContent = comment.created_at;
                var a = document.createElement('a');
                a.href = '#';
                a.classList.add('reply-link');
                var i = document.createElement('i');
                i.classList.add('lni', 'lni-reply');
                a.appendChild(i);
                a.textContent = 'Reply ( ToDo )';
                descTop.appendChild(h6);
                descTop.appendChild(span);
                descTop.appendChild(a);

                var p = document.createElement('p');
                p.textContent = comment.content;

                commentDesc.appendChild(descTop);
                commentDesc.appendChild(p);

                commentElement.appendChild(commentImg);
                commentElement.appendChild(commentDesc);

                commentsList.appendChild(commentElement);
            });
        })
        .catch(error => {
            console.error('Error fetching comments:', error);
        });
}
