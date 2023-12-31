from django.urls import path
from . import views

urlpatterns = [
    path('',  views.BookRetriveView.as_view() ),
    path('add',  views.BookAddView.as_view() ),
    path('b/<int:pk>',  views.BookRetrieveUpdateDestroyAPIView.as_view() ),
]
