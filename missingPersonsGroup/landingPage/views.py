from django.shortcuts import render

def indexPageView(request) :
    return render(request, 'landingPage/index.html')
#name html file: index.html

# Create your views here.
