'''
Authors: Megan Bates, Steven Armstrong, Kayla Tansiongco, Laura Nielson, Elise Pickett, Autumn Eaton.
Purpose: To store JSON data and display it dynamically via HTML.
'''
from django.shortcuts import render
from django.http import HttpResponse
from .models import Person

#landing page
def indexPageView(request) :
    return render(request, 'landingPage/index.html')


def individualPageView(request) :
    
   # context = {
       # "person_name": s_name
    #}
    
    return render(request, 'landingPage/individual.html')


#show individuals
def showIndividualPageView(request) :

    db_person = Person.objects.all() 

    context = {
        "data" : db_person,
    }

    return render(request, 'landingPage/individual.html', context)   

# display individual data page view
def displayIndividualPageView(request, id):
    person = Person.objects.get(id=id)

    context = {
        "data": person
    }

    return render(request, 'landingPage/displayIndividual.html', context)


# Resources
def resourcesPageView (request) :
    return render(request, 'landingPage/resources.html')

# Database
def databasePageView (request) :
    
    db_person = Person.objects.all()
    
    context = {
        "data" : db_person
    }

    return render(request, 'landingPage/database.html', context)
