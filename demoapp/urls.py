from django.urls import path 
from . import views 

app_name = 'demoapp'

urlpatterns = [ 
    # Example: http://localhost:8000/
    path('index', views.index, name='index'), 
    path('login', views.myview, name='login'),

    # Example: http://localhost:8000/getuser/John/1
    # path('getuser/<name>/<id>', views.pathview, name='pathview'), 

    # Query String Parameters
    # http://localhost:8000/getuser/?name=John&id=1 
    # path('getuser/', views.qryview, name='qryview')


    # path("showform/", views.showform, name='showform'), 
    # path("getform/", views.getform, name='getform'), 
    # path('<str:drink_name>', views.drinks, name="drink_name")
] 