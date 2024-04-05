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
            const commentsList = document.getElementById('comments-list');
            data.forEach(comment => {
                const commentElement = document.createElement('li');

                let name = "Anonymous";
                if (comment.author.first_name) {
                    name = comment.author.first_name;
                } else if (comment.author.name) {
                    name = comment.author.name;
                }
                let image = "/static/images/clients/default_profile.png";
                if (comment.author.profile_picture) {
                    image = `https://res.cloudinary.com/drjgddl0y/${comment.author.profile_picture}`
                } else if (comment.author.image) {
                    image = `https://res.cloudinary.com/drjgddl0y/${comment.author.image}`
                }

                // Create comment elements
                const commentImg = document.createElement('div');
                commentImg.classList.add('comment-img');
                const img = document.createElement('img');
                img.src = image;
                img.classList.add('rounded-circle');
                img.alt = 'img';
                commentImg.appendChild(img);

                const commentDesc = document.createElement('div');
                commentDesc.classList.add('comment-desc');

                const descTop = document.createElement('div');
                descTop.classList.add('desc-top');
                const h6 = document.createElement('h6');
                h6.textContent = name;
                const span = document.createElement('span');
                span.classList.add('date');
                span.textContent = comment.created_at;
                const a = document.createElement('a');
                a.href = '#';
                a.classList.add('reply-link');
                const i = document.createElement('i');
                i.classList.add('lni', 'lni-reply');
                a.appendChild(i);
                a.textContent = 'Reply ( ToDo )';
                descTop.appendChild(h6);
                descTop.appendChild(span);
                descTop.appendChild(a);

                const p = document.createElement('p');
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
