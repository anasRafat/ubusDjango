import geocoder
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
import folium as folium

from .forms import *
from .models import *
from django.views.generic.edit import CreateView
from geopy.geocoders import Nominatim
from geopy import distance


def cal_distance(request):


    form = measurementform(request.POST or None)
    geolocator = Nominatim(user_agent="map")
    m = folium.Map(width=800, height=500, zoom_start=4)

    if form.is_valid():
        new = form.save(commit=False)
        location_ = form.cleaned_data.get('map')
        destination_ = form.cleaned_data.get('destination')
        location = geolocator.geocode(location_)

        destination = geolocator.geocode(destination_)
        #location_cor
        l_lat = location.latitude
        l_log =location.longitude
        pointA = (l_lat, l_log)
        # print(destination)
        # distantion_cor
        d_lat = destination.latitude
        d_log = destination.longitude
        pointB = (d_lat, d_log)
        distances = distance.distance(pointA,pointB).kilometers
        m = folium.Map(width=800, height=500, location=[l_lat, l_log], zoom_start=4)
        folium.Marker(
            [l_lat, l_log], tooltip="click to see more", icon=folium.Icon(color='green')
        ).add_to(m)

        folium.Marker(
            [l_lat, l_log], tooltip="click to see more", icon=folium.Icon(color='green')
        ).add_to(m)
        folium.Marker(
            [d_lat, d_log], tooltip="click to see more", icon=folium.Icon(color='red')
        ).add_to(m)
        # draw_line
        line = folium.PolyLine(locations=[pointA, pointB], weight=5, color='blue')
        m.add_child(line)
        # distance_cal
        new.location = location
        new.distance = distances
        new.save()
    m = m._repr_html_()

    context = {
        'form': form,
        'map':m,
        'map':location,
        'destination':destination,
        'distances':distances

    }
    return render(request, 'main.html', context)


# Create your views here.
