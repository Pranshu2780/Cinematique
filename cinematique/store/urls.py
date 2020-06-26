from django.urls import path
from . import views

urlpatterns= [
    # path('',views.login,name="login"),
    # path('',views.register,name="register"),
    path('',views.home,name="home"),
    path('home/',views.home,name="home"),
    path('hollywood/',views.hollywood,name="hollywood"),
    path('bollywood/',views.bollywood,name="bollywood"),
    path('anime/',views.anime,name="anime"),
    path('web/',views.web,name="web"),
    path('newtab/<int:num>',views.newtab,name="newtab"),
    path('newtab1/<int:num>',views.newtab1,name="newtab1"),
    path('newtab2/<int:num>',views.newtab2,name="newtab2"),
    path('newtab3/<int:num>',views.newtab3,name="newtab3"),
]
