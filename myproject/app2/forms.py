from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'اكتب المهمة هنا...',
                'class': 'form-control',
            }),
        }


class TaskEditForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'is_completed']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'is_completed': forms.CheckboxInput(attrs={
                'style': 'width: auto; margin-right: 0.5rem; transform: scale(1.3);',
            }),
        }
