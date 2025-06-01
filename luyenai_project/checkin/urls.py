from django.urls import path
from . import views

app_name = 'checkin'

urlpatterns = [
    path('', views.checkin_view, name='checkin'),
]
