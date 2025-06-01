import requests
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CheckInForm

# URL Google Apps Script Web App (thay bằng URL của bạn)
GOOGLE_SCRIPT_URL = 'https://script.google.com/macros/s/AKfycbyDXCFfCS6FbX8RrzptBjTe8Xihzpwsy2sHZJekze0z690BEQaRCmFsQByGLxAzv1uOQw/exec'

def checkin_view(request):
    if request.method == 'POST':
        form = CheckInForm(request.POST)
        if form.is_valid():
            # Lấy dữ liệu từ form
            data = form.cleaned_data
            payload = {
                'full_name': data['full_name'],
                'email': data['email'],
                'note': data['note'],
            }

            try:
                # Gửi POST đến Google Apps Script API
                response = requests.post(GOOGLE_SCRIPT_URL, json=payload, timeout=10)
                result = response.json()

                if result.get('status') == 'success':
                    request.session['student_name'] = data['full_name']  # Lưu tên học sinh vào session
                    messages.success(request, 'Điểm danh thành công! Cảm ơn bạn đã tham gia.')
                    return redirect('checkin:checkin')
                else:
                    messages.error(request, 'Gặp lỗi khi lưu điểm danh: ' + result.get('message', 'Không xác định'))
            except Exception as e:
                messages.error(request, f'Không thể kết nối tới dịch vụ điểm danh: {e}')
        else:
            messages.error(request, 'Vui lòng kiểm tra lại thông tin nhập.')
    else:
        form = CheckInForm()

    return render(request, 'checkin/checkin.html', {'form': form})


