from django.urls import path
from .views import odd_even_view

urlpatterns = [
    path("odd-even/", odd_even_view, name="odd_even")
]
