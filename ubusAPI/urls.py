from django.urls import path
from ubusAPI import views
from .views import MyTokenObtainPairView
from rest_framework_simplejwt.views import (
    TokenRefreshView,)
app_name = 'ubusAPI'

urlpatterns = [
    path('', views.RoutesAPI.as_view()),
    path('', views.StationAPI.as_view()),
    path('', views.BusAPI.as_view()),
    path('', views.DriverAPI.as_view()),
    path('', views.RoutesStationAPI.as_view()),
    path('', views.UserTicketAPI.as_view()),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh')

]