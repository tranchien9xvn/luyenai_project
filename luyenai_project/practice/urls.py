from django.urls import path
from . import views
from django.urls import path
from . import views


app_name = 'practice'

urlpatterns = [
    path('', views.practice_home, name='practice_home'),  # Chọn tuần học
    #path('', views.practice_home, name='practice_home'),

    path('upload/', views.upload_exercise, name='upload_exercise'),  # Upload bài tập có bảo mật

    #path('', views.practice_home, name='practice_home'),

    path('week/<int:week_number>/', views.exercise_list, name='exercise_list'),  # Chọn bài tập
    path('week/<int:week_number>/exercise/<int:exercise_id>/', views.do_exercise, name='do_exercise'),  # Làm bài tập
]
