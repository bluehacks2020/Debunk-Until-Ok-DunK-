from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView


def home(request):
    return render(request,'main/home.html')
    
def samples(request):
    return render(request, 'main/samples.html')

def about(request):
    return render(request, 'main/about.html')

def donate(request):
    return render(request, 'main/donate.html')

def partner(request):
    return render(request, 'main/partner.html')



class HomeView(TemplateView):
    template_name ='home.html'

# Create your views here.
