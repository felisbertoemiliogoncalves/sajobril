from django.urls import path , include

from visitor import views


app_name = "vizitor"
urlpatterns = [
    path('', views.index, name='index'),
    path('atividade', views.atividade, name='atividade'),
    path('konaba', views.konaba, name='konaba'),
    path('misa', views.misa, name='misa'),
    path('eventu', views.eventu, name='eventu'),
    path('anunsiu', views.anunsiu, name='anunsiu'),
    path('atendimentu', views.atendimentu, name='atendimentu'),
    path('planu', views.planu, name='planu'),
    path('detallu', views.detallu, name='detallu'),


                     
]


    
