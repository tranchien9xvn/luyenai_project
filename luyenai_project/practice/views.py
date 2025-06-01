from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Week, Exercise, Question
import requests

GOOGLE_SCRIPT_URL = 'https://script.google.com/macros/s/AKfycbyDXCFfCS6FbX8RrzptBjTe8Xihzpwsy2sHZJekze0z690BEQaRCmFsQByGLxAzv1uOQw/exec'  # thay bằng URL thực
'''
def practice_home(request):
    weeks = Week.objects.order_by('number')
    return render(request, 'practice/home.html', {'weeks': weeks})
'''

from django.shortcuts import render
from .models import Week

def practice_home(request):
    weeks = Week.objects.order_by('number')
    return render(request, 'practice/home.html', {'weeks': weeks})



def exercise_list(request, week_number):
    week = get_object_or_404(Week, number=week_number)
    exercises = Exercise.objects.filter(week=week)
    return render(request, 'practice/exercise_list.html', {'week': week, 'exercises': exercises})

def do_exercise(request, week_number, exercise_id):
    week = get_object_or_404(Week, number=week_number)
    exercise = get_object_or_404(Exercise, pk=exercise_id, week=week)
    questions = Question.objects.filter(exercise=exercise)

    if request.method == 'POST':
        answers = []
        for question in questions:
            answer_text = request.POST.get(f'question_{question.id}', '').strip()
            answers.append((question, answer_text))

        # Gửi từng câu trả lời lên Google Sheets Sheet2 qua Google Apps Script
        student_name = request.session.get('student_name', 'Unknown')

        all_success = True
        for question, answer in answers:
            payload = {
                'student_name': student_name,
                'week': str(week.number),
                'exercise_title': exercise.title,
                'question_text': question.text,
                'answer_text': answer,
            }
            try:
                response = requests.post(GOOGLE_SCRIPT_URL, json=payload, timeout=10)
                result = response.json()
                if result.get('status') != 'success':
                    all_success = False
                    messages.error(request, f"Lỗi khi gửi câu hỏi: {question.text[:30]}...")
                    break
            except Exception as e:
                all_success = False
                messages.error(request, f"Lỗi kết nối dịch vụ: {e}")
                break

        if all_success:
            messages.success(request, 'Nộp bài thành công! Cảm ơn bạn đã luyện tập.')
            return redirect('practice:practice_home')

    return render(request, 'practice/do_exercise.html', {
        'week': week,
        'exercise': exercise,
        'questions': questions,
    })

# practice/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Week, Exercise, Question
from .forms import UploadExerciseForm

SECURITY_CODE = "12345"  # Bạn có thể lưu trong settings hoặc DB để dễ thay đổi

def upload_exercise(request):
    if request.method == 'POST':
        form = UploadExerciseForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['security_code']
            if code != SECURITY_CODE:
                messages.error(request, "Mã bảo mật không đúng!")
            else:
                week_number = form.cleaned_data['week_number']
                week_title = form.cleaned_data['week_title']
                exercise_title = form.cleaned_data['exercise_title']
                questions_text = form.cleaned_data['questions']

                week, created = Week.objects.get_or_create(number=week_number, defaults={'title': week_title})
                if not created and week.title != week_title:
                    # Cập nhật tên tuần nếu khác
                    week.title = week_title
                    week.save()

                exercise = Exercise.objects.create(week=week, title=exercise_title)

                for line in questions_text.strip().split('\n'):
                    if line.strip():
                        Question.objects.create(exercise=exercise, text=line.strip())

                messages.success(request, "Tải bài tập lên thành công!")
                return redirect('practice:upload_exercise')
    else:
        form = UploadExerciseForm()

    return render(request, 'practice/upload_exercise.html', {'form': form})
