
from django.urls import path
from .views import *



urlpatterns = [
    path("post/",create),
    path("get/", drive_get),
    path("delete/<str:name>/",drive_delete),
    path("update/<str:name>/", update),
    path("register/",  register),
    # path("get_driver/", driver_get),
    path("login/",LoginView.as_view())

]