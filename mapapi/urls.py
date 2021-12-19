
from django.urls import path
from .views import *


urlpatterns = [
    path("post/",create),
    path("get/", drive_get),
    path("detial/<str:name>/",drive_det),
    path("update/<str:name>/", update)

]