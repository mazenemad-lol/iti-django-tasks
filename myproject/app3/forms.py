from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'notes']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'الاسم بالكامل...',
                'class': 'form-control',
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'example@domain.com',
                'class': 'form-control',
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': 'رقم الهاتف (اختياري)...',
                'class': 'form-control',
            }),
            'notes': forms.Textarea(attrs={
                'placeholder': 'ملاحظات إضافية (اختياري)...',
                'rows': 3,
                'class': 'form-control',
            }),
        }
