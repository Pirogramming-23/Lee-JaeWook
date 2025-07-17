from django.db import models
from django.contrib.auth.models import User

# 임시로 만든 field
# DEVTOOL_CHOICES = [
#     ('django', 'Django'),
#     ('flask', 'Flask'),
#     ('react', 'React'),
#     ('vue', 'Vue'),
#     ('spring', 'Spring'),
# ]

class Idea(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='idea_thumbnails/', blank=True, null=True)
    interest = models.IntegerField(default=0)
    # devtool = models.CharField(max_length=20, choices=DEVTOOL_CHOICES, default='django')
    devtool = models.ForeignKey('DevTool', on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
class IdeaStar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    idea = models.ForeignKey('Idea', on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = ('user', 'idea')
        
class DevTool(models.Model):
    name = models.CharField(max_length=30, unique=True)
    kind = models.CharField(max_length=50)
    content = models.TextField()
    
    def __str__(self):
        return self.name