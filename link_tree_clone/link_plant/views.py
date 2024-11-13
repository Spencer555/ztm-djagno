from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy

from link_plant.models import Profile, Links
# Create your views here.


class LinkListView(ListView):
    model = Links
    queryset = Links.objects.all()
    template_name = 'link_list.html'


class LinkCreateView(CreateView):
    model = Links
    success_url = reverse_lazy('link_lists')
    fields = "__all__"
    template_name = 'link_create.html'

class LinkUpdateView(UpdateView):
    model = Links
    success_url = reverse_lazy('link_lists')
    fields = ["text", "url"]
    template_name = 'link_create.html'
    
    
class LinkDeleteView(DeleteView):
    model = Links
    success_url = reverse_lazy('link_lists')
    template_name = 'link_delete.html'
    
    
    
def profile_view(request, profile_slug):
    profile = get_object_or_404(Profile, slug=profile_slug)
    links = profile.links.all()
    
    context = {
        'profile':profile,
        'links':links
    }
    
    
    return render(request, 'profile.html', context)