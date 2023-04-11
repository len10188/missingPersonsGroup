from django.shortcuts import render
from django.http import HttpResponse

def indexPageView(request) :
    return render(request, 'landingPage/index.html')
#name html file: index.html

# Create your views here.
