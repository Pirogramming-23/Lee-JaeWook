from django.db import models

# 게시글을 업로드하는 함수 테이블에 있는 필드값을 채움
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    like_count = models.PositiveIntegerField(default=0)

# 댓글을 달 수 있게 하는 함수 외래값을 가져와서 코멘트를 달 수 있게 함
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

