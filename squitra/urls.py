from django.urls import path

from . import views

app_name='squap'

urlpatterns = [
        path('map/', views.view_map, name = 'map'),
        path('',views.view_main, name = 'main'),
        path('sightings/',views.sightings_view, name = 'sightings'),
        path('sightings/stats', views.stats_view, name = 'stats'),
        path('sightings/<str:Unique_Squirrel_ID>/',views.update_squirrel_view,name='edit_sighting'),
        path('sightings/add',views.add_squirrel_view,name='add_sighting'),
        ]
