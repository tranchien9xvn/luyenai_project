from django.shortcuts import redirect
from django.utils import timezone
import requests
from django.contrib import messages

GOOGLE_SCRIPT_URL = 'https://script.google.com/macros/s/AKfycbyDXCFfCS6FbX8RrzptBjTe8Xihzpwsy2sHZJekze0z690BEQaRCmFsQByGLxAzv1uOQw/exec'
CHATGPT_URL = 'https://chatgpt.com/g/g-6804a583b05481918e69fa545ecbf4f1-thay-chien'

def chat_with_ai(request):
    student_name = request.session.get('student_name')
    if not student_name:
        messages.error(request, "Bạn cần điểm danh trước khi trò chuyện với AI.")
        return redirect('checkin:checkin_home')

    payload = {
        'name': student_name,
        'start_time': timezone.now().isoformat()
    }
    try:
        response = requests.post(GOOGLE_SCRIPT_URL, json=payload, timeout=10)
        resp_json = response.json()
        if resp_json.get('status') != 'success':
            messages.warning(request, 'Lưu thông tin chat thất bại, nhưng vẫn chuyển tiếp.')
    except Exception as e:
        messages.warning(request, f'Không thể kết nối lưu thông tin chat: {e}')
    print("Response from GAS:", response.text)
    return redirect(CHATGPT_URL)


