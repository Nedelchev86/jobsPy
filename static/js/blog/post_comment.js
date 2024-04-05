
document.addEventListener("DOMContentLoaded", function () {
    const commentForm = document.getElementById("comment-form");
    commentForm.addEventListener("submit", function (event) {
        event.preventDefault();

        // Get the comment content from the form
        const content = document.getElementById("comment-content").value;
        const blogPostId = window.location.pathname.split("/")[2];

        // Send the comment data to the backend
        postComment(content);
    });
});

function postComment(content) {
    const blogPostId = window.location.pathname.split("/")[2];
    // AJAX request to post the comment
    fetch(`/api/blog/${blogPostId}/comments/`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": CSRF_TOKEN,
            // Add any required authentication headers if needed
        },
        body: JSON.stringify({content: content}),
    })
        .then((response) => response.json())
        .then((data) => {
            document.getElementById("comment-content").value = "";
            document.getElementById("comments-list").innerHTML = "";
            loadComment(blogPostId);
        })
        .catch((error) => {
            console.error("Error posting comment:", error);
        });
}

function loadComment(blogPostId) {
    fetch(`/api/blog/${blogPostId}/comments/`)
        .then((response) => response.json())
        .then((data) => {
            const commentNumber = document.getElementById("comment-number");
            commentNumber.textContent = `${data.length} comments`;

            const commentsList = document.getElementById("comments-list");
            data.forEach((comment) => {
                const commentElement = document.createElement("li");

                let name = "Anonymous";
                if (comment.author.first_name) {
                    name = comment.author.first_name;
                } else if (comment.author.name) {
                    name = comment.author.name;
                }
                let image = "/static/images/clients/default_profile.png";
                if (comment.author.profile_picture) {
                    image = `https://res.cloudinary.com/drjgddl0y/${comment.author.profile_picture}`;
                } else if (comment.author.image) {
                    image = `https://res.cloudinary.com/drjgddl0y/${comment.author.image}`;
                }

                commentElement.innerHTML = `
                    <div class="comment-img">
                        <img src=${image} class="rounded-circle" alt="img">
                    </div>
                    <div class="comment-desc">
                        <div class="desc-top">
                            <h6>${name}</h6>
                            <span class="date">${comment.created_at}</span>
                            <a href="#" class="reply-link"><i class="lni lni-reply"></i>Reply /ToDo/</a>
                        </div>
                        <p>
                            ${comment.content}
                        </p>
                    </div>
                `;

                commentsList.appendChild(commentElement);
            });
        })
        .catch((error) => {
            console.error("Error fetching comments:", error);
        });
}
