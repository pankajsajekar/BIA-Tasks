from django.urls import path
from . import views

urlpatterns = [
    path('', views.UploadVideoView.as_view()),
]
