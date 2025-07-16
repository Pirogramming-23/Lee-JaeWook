from django import forms
from .models import Idea, DevTool

class IdeaForm(forms.ModelForm):
    class Meta:
        model = Idea
        fields = ['title', 'image', 'content', 'interest', 'devtool']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 5}),
            'devtool': forms.Select(),
        }
        
class DevToolForm(forms.ModelForm):
    class Meta:
        model = DevTool
        fields = ['name', 'kind', 'content']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': '이름'}),
            'kind': forms.TextInput(attrs={'placeholder': '종류'}),
            'content': forms.Textarea(attrs={'placeholder': '개발툴 설명'}),
        }