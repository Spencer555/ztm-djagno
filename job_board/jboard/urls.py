from django.urls import path 
from jboard.views import index,  job_detail



urlpatterns = [
    path('', index, name="index"),
    path('job/<int:id>/', job_detail, name="job-detail"),
    path('job/<int:id>/', job_detail, name="job-detail"),
]
