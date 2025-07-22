from django import forms
from .models import Post

# 테이블에서 필드 3개만 추가 제목, 내용, 이미지
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'class': 'form-input'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-input'}),
        }
