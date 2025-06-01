from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('checkin/', include('checkin.urls')),  # app điểm danh
    path('', include('main.urls')),  # app chính
    path('practice/', include('practice.urls')),  # app luyện tập
    path('chatforteacher/', include('chatforteacher.urls')),

    # Xóa hoặc đổi tên view 'practice' nếu có ở main.views
]
