from django.shortcuts import render
from .models import job


# Create your views here.
def job_list(requests):
    jobs_list = job.objects.all()
    context = {'jobs': jobs_list}
    return render(requests, 'job/job_list.html', context)


def job_detail(request, id):
    job_details = job.objects.get(id=id)
    context = {'job': job_details}
    return render(request, 'job/job_detail.html', context)
