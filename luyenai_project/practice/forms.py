from django import forms
from .models import Question

class PracticeForm(forms.Form):
    # form động sẽ được tạo trong view
    pass


# practice/forms.py
from django import forms
from .models import Week, Exercise, Question

class UploadExerciseForm(forms.Form):
    security_code = forms.CharField(label='Mã bảo mật', max_length=100, widget=forms.PasswordInput)
    week_number = forms.IntegerField(label='Tuần học')
    week_title = forms.CharField(label='Tiêu đề tuần', max_length=100)
    exercise_title = forms.CharField(label='Tiêu đề bài tập', max_length=200)
    questions = forms.CharField(label='Danh sách câu hỏi', widget=forms.Textarea,
                                help_text='Nhập mỗi câu hỏi một dòng')
