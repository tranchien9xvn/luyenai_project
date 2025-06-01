from django.shortcuts import render, redirect
from django.contrib import messages

def index(request):
    return render(request, 'main/index.html')

from django.shortcuts import redirect

def practice(request):
    return redirect('practice:practice_home')

def chatgpt(request):
    # Thay bằng URL thực ChatGPT custom của bạn
    return redirect('https://chat.openai.com/g/your-custom-gpt-id')

def daily_checkin(request):
    if request.method == 'POST':
        # TODO: Xử lý logic điểm danh, lưu DB nếu cần
        messages.success(request, 'Điểm danh thành công! Tiếp tục luyện tập để tăng đẳng cấp.')
        return redirect('main:index')
    return redirect('main:index')

def logout_view(request):
    # Đây chỉ ví dụ redirect về home
    return redirect('main:index')
