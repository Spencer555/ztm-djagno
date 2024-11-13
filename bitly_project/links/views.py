from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from links.forms import LinkForm
from links.models import Link
# Create your views here.
def index(request):
    links = Link.objects.all()
    context = {
        'links':links
    }
    return render(request, 'links\index.html',  context)


def root_link(request, link_slug):
    
    link = get_object_or_404(Link, slug=link_slug)
    link.click()#increment the clicked field 
    
    
    return redirect(link.url)




def add_link(request):
    if request.method == 'POST':
        # form has data 
        form = LinkForm(request.POST)
        if form.is_valid():
            # process data 
            # save data and return user to home page
            form.save()
            return redirect(reverse('home'))
        
            
    else:
        form = LinkForm()
    context = {
        "form":form
    }
    
    
        
    return render(request, 'links\create.html', context)