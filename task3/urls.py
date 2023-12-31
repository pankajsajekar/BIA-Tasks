from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListCreateView.as_view()),
    path('<int:pk>', views.PostRetrieveUpdateDestroyView.as_view()),
]
