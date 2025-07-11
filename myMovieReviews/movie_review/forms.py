from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [
            'title',        # 제목
            'year',         # 개봉년도
            'genre',        # 장르
            'rating',       # 별점
            'running_time', # 러닝타임
            'content',      # 리뷰 내용
            'director',     # 감독
            'actor',        # 배우
            'img'           # 이미지
        ]
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': '제목을 입력하세요'}),
            'year': forms.NumberInput(attrs={
                    'placeholder': 'YYYY',
                    'value': 2025  # 기본값 설정
                }),
            'genre': forms.Select(),  # 선택형 (CharField + choices 설정 가정)
            'rating': forms.NumberInput(attrs={
            'placeholder': '1~5',
            'min': 1,
            'max': 5,
            'step': 0.5,
                }),
            'running_time': forms.NumberInput(attrs={'placeholder': '분 단위 입력'}),
            'content': forms.Textarea(attrs={'rows': 8, 'placeholder': '리뷰 내용을 입력하세요'}),
            'director': forms.TextInput(attrs={'placeholder': '감독 이름'}),
            'actor': forms.TextInput(attrs={'placeholder': '배우 이름'}),
            'img' : forms.FileInput(),
        }
