from django.urls import path
from accounts import views

urlpatterns = [
    path('', views.UsersAPI.as_view()),
]