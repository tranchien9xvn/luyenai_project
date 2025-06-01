from django import forms
from .models import CheckIn

class CheckInForm(forms.ModelForm):
    class Meta:
        model = CheckIn
        fields = ['full_name', 'email', 'note']
        widgets = {
                    'full_name': forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Nhập họ và tên'}),
                    'email': forms.EmailInput(attrs={'class': 'input-field', 'placeholder': 'Nhập email'}),
                    'note': forms.Textarea(attrs={'class': 'input-field', 'placeholder': 'Ghi chú (tùy chọn)', 'rows': 3}),
                }
