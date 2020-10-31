from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'hood/dashboard.html')

def systemadmin(request):
    return render(request, 'hood/systemadmin.html')

def neighbourhoodadmin(request):
    return render(request, 'hood/neighbourhoodadmin.html')   