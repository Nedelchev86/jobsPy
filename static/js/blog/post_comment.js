document.addEventListener('DOMContentLoaded', function () {
    const commentForm = document.getElementById('comment-form');

    commentForm.addEventListener('submit', function (event) {
        event.preventDefault();

        // Get the comment content from the form
        const content = document.getElementById('comment-content').value;
            const blogPostId = window.location.pathname.split('/')[2]



        // Send the comment data to the backend
        postComment(content);
    });
});

function postComment(content) {
    const blogPostId = window.location.pathname.split('/')[2]
         const csrfToken = "{{ csrf_token }}";
         console.log(csrfToken)
    // AJAX request to post the comment
    fetch(`/api/blog/${blogPostId}/comments/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
               'X-CSRFToken':  csrfToken,
            // Add any required authentication headers if needed
        },
        body: JSON.stringify({ content: content }),
    })
    .then(response => response.json())
    .then(data => {
        // Comment successfully posted, update UI
        console.log('Comment posted:', data);
        // You can update the UI to display the new comment here
    })
    .catch(error => {
        console.error('Error posting comment:', error);
    });
}