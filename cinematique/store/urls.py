from django.urls import path
from . import views

urlpatterns= [
    path('',views.home,name="home"),
    path('home/',views.home,name="home"),
    path('hollywood/',views.hollywood,name="hollywood"),
    path('bollywood/',views.bollywood,name="bollywood"),
    path('anime/',views.anime,name="anime"),
    path('web/',views.web,name="web"),
]
