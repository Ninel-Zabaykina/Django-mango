from django.urls import path
from .views import Second

urlpatterns = [
    path('second', Second.as_view()),
]

