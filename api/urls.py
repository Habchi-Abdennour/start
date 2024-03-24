from . import views
from django.urls import path

urlpatterns = [
    path('',views.hello ),
     path('api/',views.send ),



]
