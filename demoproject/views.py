from django.http import HttpResponse, HttpResponseNotFound

def handler404(request, exception):
    return HttpResponse('404: Page is not found')

def home(request):
    return HttpResponseNotFound('HIHIHIH')