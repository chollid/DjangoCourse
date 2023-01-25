from django.shortcuts import render

from django.http import HttpResponse 

from django.http import HttpResponsePermanentRedirect 
from django.urls import reverse 


def index(request): 
    content = '<html><body><h1>Hello, world. This is the index view of SIIIIKE.</h1><h2>BOOOOGU GOOOOGU</h2><button onclick=(alert(window.innerWidth))>Press me</button></body></html>'
    return HttpResponse(content) 

def myview(request):
    return HttpResponsePermanentRedirect(reverse('demoapp:login'))

# def index(request): 
#     path = request.path 
#     method = request.method 
#     content=''' 
# <center><h2>Testing Django Request Response Objects</h2> s
# <p>Request path : " {}</p> 
# <p>Request Method :{}</p></center> 
# '''.format(path, method) 
#     return HttpResponse(content) 

# Example: http://localhost:8000/getuser/John/1
# def pathview(request, name, id): 
#     return HttpResponse("Name:{} UserID:{}".format(name, id)) 

# Query String Parameters
# Example: http://localhost:8000/getuser/?name=John&id=1 
# def qryview(request): 
#     name = request.GET['name'] 
#     id = request.GET['id'] 
#     return HttpResponse("Name:{} UserID:{}".format(name, id)) 

# Render form.html
# def showform(request): 
#     return render(request, 'form.html')

# def getform(request): 
#     if request.method == "POST": 
#         id=request.POST['id'] 
#         name=request.POST['name'] 
#         return HttpResponse("Name:{} UserID:{}".format(name, id))

# def drinks(request, drink_name): 
#     drink = {
#         'mocha': 'type of coffe',
#         'tea': 'type of beverage',
#         'lemonade': 'type of refreshment',
#     }

#     choice_of_drink = drink[drink_name]

#     return HttpResponse(f"<h2> {drink_name} </h2> {choice_of_drink}")