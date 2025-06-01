from django.urls import path
from . import views

app_name = 'chatforteacher'

urlpatterns = [
    path('chat/', views.chat_with_ai, name='chat_with_ai'),
]
