from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .models import * 
# Create your views here.

# def login(request):
#     if request.method=='POST':
#        username = request.POST['username']
#        password = request.POST['password']

#        user = auth.authenticate(username=username,password=password)

#        if user is not None:
#            auth.login(request,user)
#            return redirect("/")
#        else:
#            messages.info(request,'invalid credentials')
#            return redirect('login')    
#     else:
#         return render(request,'login.html')

def home(request):
    context = {}
    return render(request,'store/home.html',context)

    
def hollywood(request):
    context = {}
    return render(request,'store/hollywood.html',context)

    
def bollywood(request):
    context = {}
    return render(request,'store/bollywood.html',context)

    
def anime(request):
    items = Anime.objects.all()
    context = {'items':items}
    return render(request,'store/anime.html',context)

    
def web(request):
    context = {}
    return render(request,'store/web.html',context)

def newtab(request,num):
    

    



    data=Anime.objects.filter(id=num)
    print(data)

    for i in data:
        print(i.ratings)
    context = {'anime':data}
    return render(request,'store/newtab.html',context)