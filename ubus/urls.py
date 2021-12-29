
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from linesStops.views import Linesview , stationsview , Cordsview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('users.urls')),

    path('mapapi/', include('mapapi.urls')),
    path('lines/',Linesview.as_view()),
    path('stations/',stationsview.as_view()),
    path('cords/',Cordsview.as_view()),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
