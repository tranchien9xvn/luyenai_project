from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('chatgpt/', views.chatgpt, name='chatgpt'),
    path('daily-checkin/', views.daily_checkin, name='daily_checkin'),
    path('logout/', views.logout_view, name='logout'),
]
