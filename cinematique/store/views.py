from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .models import * 
# Create your views here.

# def register(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         email = request.POST['email']
#         password1 = request.POST['password1']
#         password2 = request.POST['password2']
#         user = user.objects.create_user(username=username,password=password1,email=email)
#         user.save();
#         print('user created')
#         return redirect("/")
#     else:
#         return render(request,'store/register.html')
    
    



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
    items = Hollywood.objects.all()
    context = {'items':items}
    return render(request,'store/hollywood.html',context)
    
def bollywood(request):
    items = Bollywood.objects.all()
    context = {'items':items}
    return render(request,'store/bollywood.html',context)

    
def anime(request):
    items = Anime.objects.all()
    context = {'items':items}
    return render(request,'store/anime.html',context)

    
def web(request):
    items = Web.objects.all()
    context = {'items':items}
    return render(request,'store/web.html',context)

def newtab(request,num):
    data=Anime.objects.filter(id=num)
    print(data)
    for i in data:
        print(i.ratings)
    context = {'anime':data}
    return render(request,'store/newtab.html',context)

    
def newtab1(request,num):
    data=Web.objects.filter(id=num)
    print(data)
    for i in data:
        print(i.ratings)
    context = {'web':data}
    return render(request,'store/newtab1.html',context)

       
def newtab2(request,num):
    data=Bollywood.objects.filter(id=num)
    print(data)
    for i in data:
        print(i.ratings)
    context = {'bollywood':data}
    return render(request,'store/newtab2.html',context)

          
def newtab3(request,num):
    data=Hollywood.objects.filter(id=num)
    print(data)
    for i in data:
        print(i.ratings)
    context = {'hollywood':data}
    return render(request,'store/newtab3.html',context)