from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
from trips.models import Trip, Note

class HomeView(TemplateView):
    template_name = 'trip/index.html'
    
    
    
    
    
    
    
def trips_list(request):
    trips = Trip.objects.filter(owner=request.user)
    
    context = {
        'trips': trips
    }
    
    return render(request, 'trip/trips_list.html', context)