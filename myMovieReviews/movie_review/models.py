from django.db import models

GENRE_CHOICES = [
    ('action', '액션'),
    ('comedy', '코미디'),
    ('drama', '드라마'),
    ('thriller', '스릴러'),
    ('romance', '로맨스'),
]

# models.py
class Review(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    content = models.TextField()
    rating = models.IntegerField()
    img = models.ImageField(upload_to='review_images/', blank=True, null=True)

    genre = models.CharField(max_length=20, choices=GENRE_CHOICES)
    running_time = models.IntegerField()
    year = models.IntegerField()
    actor = models.CharField(max_length=200)
    director = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
