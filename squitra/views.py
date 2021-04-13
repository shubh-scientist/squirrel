from django.shortcuts import render
from .models import Squirrel

def view_map(request):
    sightings = Squirrel.objects.all()[:100]
    context = {
            'sightings': sightings,
            }
    return render( request, 'squitra/map.html', context)
