from django.urls import path

from . import views

app_name='squap'

urlpatterns = [
        path('map/', views.view_map, name='map'),
        ]
