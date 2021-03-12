from django.shortcuts import render
from django.views import generic

from .models import Service, About


# Create your views here.
class ServiceList(generic.ListView):
    model = Service
    template_name = 'services/service_list.html'


class ServiceDetail(generic.DetailView):
    """ detail view of services """
    model = Service
    template_name = 'services/service_detail.html'


class AboutPage(generic.TemplateView):
    """ detail view of services """
    template_name = 'services/about.html'
    
