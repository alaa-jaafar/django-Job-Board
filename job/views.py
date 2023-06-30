

from django.shortcuts import render
from .models import Job
from django.core.paginator import Paginator


# Create your views here.
def job_list(requests):
    jobs_list = Job.objects.all()
    paginator = Paginator(jobs_list, 1)
    page_number = requests.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {'jobs': page_obj}
    return render(requests, 'job/job_list.html', context)


def job_detail(request, id):
    job_details = Job.objects.get(id=id)
    context = {'job': job_details}
    return render(request, 'job/job_detail.html', context)
