document.addEventListener("DOMContentLoaded", function () {
    // 댓글 작성
    const commentButtons = document.querySelectorAll(".comment-submit");

    commentButtons.forEach((button) => {
        button.addEventListener("click", function () {
            const postId = this.dataset.postId;
            const input = document.querySelector(`.comment-input[data-post-id="${postId}"]`);
            const content = input.value;

            if (!content.trim()) return;

            fetch("/comment/create/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/x-www-form-urlencoded"
                },
                body: `post_id=${postId}&content=${encodeURIComponent(content)}`
            })
            .then(res => res.json())
            .then(data => {
                if (data.content) {
                    const ul = document.getElementById(`comment-list-${postId}`);
                    const li = document.createElement("li");
                    li.id = `comment-${data.id}`;
                    li.innerHTML = `
                        ${data.content}
                        <button class="comment-delete" data-comment-id="${data.id}">삭제</button>
                    `;
                    ul.appendChild(li);
                    input.value = "";
                    bindDeleteButtons();  // 새로 추가된 버튼에도 이벤트 연결
                }
            });
        });
    });

    // 댓글 삭제
    function bindDeleteButtons() {
        const deleteButtons = document.querySelectorAll(".comment-delete");

        deleteButtons.forEach(button => {
            button.onclick = function () {
                const commentId = this.dataset.commentId;
                fetch(`/comment/${commentId}/delete/`, {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/x-www-form-urlencoded"
                    }
                })
                .then(res => res.json())
                .then(data => {
                    if (data.status === "deleted") {
                        const li = document.getElementById(`comment-${commentId}`);
                        if (li) li.remove();
                    }
                });
            };
        });
    }

    // 페이지 처음 로딩될 때도 삭제 버튼에 이벤트 연결
    bindDeleteButtons();
});

// 좋아요 기능
function likePost(postId) {
    fetch(`/${postId}/like/`, {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded"
        }
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById(`like-count-${postId}`).innerText = data.like_count;
    });
}
