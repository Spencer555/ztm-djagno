from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, DetailView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
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

class TripCreateView(CreateView):
    model = Trip
    success_url = reverse_lazy('trip-list')
    fields = ['city', 'country', 'start_date', 'end_date']
    template_name = 'trip/trip_create.html'
    
    
    
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
    
    
    
class TripDetailView(DetailView):
    
    model = Trip 
    template_name = 'trip/trip_detail.html'
    
    
    # data stored on Trip also have notes data 
    # adding the notes to the trip
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        trip = context['object']
        notes = trip.notes.all()
        context['notes'] = notes 
        return context
    
    
    

class NoteDetailView(DetailView):
    model = Note
    template_name = 'trip/note_detail.html'
    
    
    
    
class NoteListView(ListView):
    model = Note
    template_name='trip/note_list.html'
    
    
    
    def get_queryset(self):
        queryset = Note.objects.filter(trip__owner=self.request.user)
        return queryset
    
    
    
    
class NoteCreateView(CreateView):
        
    model = Note 
    success_url = reverse_lazy('note-list')
    fields = '__all__'
    template_name = 'trip/note_create.html'
    
    
    def get_form(self):
        form = super(NoteCreateView, self).get_form()
        trips = Trip.objects.filter(owner=self.request.user)
        
        # modify form to get the trips for the logged in user
        form.fields['trip'].queryset = trips
        return form 
    
    
class NoteUpdateView(UpdateView):
        
    model = Note 
    success_url = reverse_lazy('note-list')
    fields = '__all__'
    template_name = 'trip/note_create.html'
    
    
    def get_form(self):
        form = super(NoteUpdateView, self).get_form()
        trips = Trip.objects.filter(owner=self.request.user)
        
        # modify form to get the trips for the logged in user
        form.fields['trip'].queryset = trips
        return form 
    
class NoteDeleteView(DeleteView):
        
    model = Note 
    success_url = reverse_lazy('note-list')
    # no template needed
    # send a post req to url
    
class TripUpdateView(UpdateView):
        
    model = Trip 
    success_url = reverse_lazy('trip-list')
    fields = ['city', 'country', 'start_date', 'end_date']
    template_name = 'trip/trip_create.html'
    
    
    
class TripDeleteView(DeleteView):
        
    model = Trip
    success_url = reverse_lazy('trip-list')
    # no template needed
    # send a post req to url
