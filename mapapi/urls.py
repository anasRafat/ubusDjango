from django.urls import path
from .views import *


urlpatterns = [
    path("",mapview.as_view())

]