from django.shortcuts import render, HttpResponse, get_object_or_404

# Create your views here.
from jboard.models import JobPosting




def index(request):
    active_jobs = JobPosting.objects.filter(is_active=True)
    
    context = {
        'active_jobs': active_jobs
    }
    
    return render(request, 'job_board/index.html', context)






def job_detail(request, id):
    
    job = get_object_or_404(JobPosting, id=id)
    
    context = {'job':job}
    
    return render(request, 'job_board/job_detail.html', context)