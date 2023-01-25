from django.shortcuts import render

from django.http import HttpResponse 


def index(request): 
    content = '<html><body><h1>Hello, world. This is the index view of SIIIIKE.</h1><h2>BOOOOGU GOOOOGU</h2><button onclick=(alert(window.innerWidth))>Press me</button></body></html>'
    return HttpResponse(content) 