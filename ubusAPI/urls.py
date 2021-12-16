from django.urls import path
from ubusAPI import views

app_name = 'ubusAPI'

urlpatterns = [
    path('', views.RoutesAPI.as_view()),
    path('', views.StationAPI.as_view()),
    path('', views.BusAPI.as_view()),
    path('', views.DriverAPI.as_view()),
    path('', views.RoutesStationAPI.as_view()),
    path('', views.UserTicketAPI.as_view()),

]