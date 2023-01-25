from django.urls import path 
from . import views 

app_name = 'newapp'

urlpatterns = [ 
    # Example: http://localhost:8000/
    path('index_1', views.index, name='index'), 
]