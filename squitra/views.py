from django.shortcuts import render,redirect
from .models import Squirrel
from django.http import HttpResponse
from .forms import SquirForm

def view_map(request):
    sightings = Squirrel.objects.all()[:100]
    context = {
            'sightings': sightings,
            }
    return render( request, 'squitra/map.html', context)

def view_main(request):
    return render(request,'squitra/main.html',)

def sightings_view(request):
    squirrels=Squirrel.objects.all()
    context={
        'squirrels':squirrels,
        }
    return render(request,'squitra/sightings.html',context)

def stats_view(request):
    total_count = len(Squirrel.objects.all())
    above_ground_count = len( Squirrel.objects.filter(Location = 'Above Ground'))
    climbing_count = len( Squirrel.objects.filter(Climbing = True))
    running_count = len( Squirrel.objects.filter(Running = True))
    eating_count = len( Squirrel.objects.filter(Eating = True))
    black_count = len( Squirrel.objects.filter(Primary_Fur_Color = 'Black'))
    gray_count = len( Squirrel.objects.filter(Primary_Fur_Color = 'Gray'))
    cinnamon_count = len( Squirrel.objects.filter(Primary_Fur_Color = 'Cinnamon'))
    context = {'total_count' : total_count,
              'above_ground_count' : above_ground_count,
              'running_count': running_count,
              'eating_count': eating_count,
              'climbing_count' : climbing_count,
              'black_count' : black_count,
              'gray_count' : gray_count,
              'cinnamon_count' : cinnamon_count,
              }
    return render(request, 'squitra/stats.html', context)

def update_squirrel_view(request,Unique_Squirrel_ID):
    squirrel=Squirrel.objects.get(Unique_Squirrel_ID=Unique_Squirrel_ID)
    if request.method=="POST":
        form=SquirForm(request.POST, instance=squirrel)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings')

    else:
        form =SquirForm(instance=squirrel)
    context={
            'form':form
        }
    return render(request,'squitra/edit.html',context)

def add_squirrel_view(request):
    if request.method=="POST":
        form=SquirForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings')

    else:
        form=SquirForm()
    context={
            'form':form,
        }
    return render(request,'squitra/edit.html',context)

