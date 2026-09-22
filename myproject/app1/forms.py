from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'اكتب عنوان المقال هنا...',
                'class': 'form-control',
            }),
            'content': forms.Textarea(attrs={
                'placeholder': 'اكتب محتوى المقال هنا...',
                'rows': 4,
                'class': 'form-control',
            }),
        }
