from django.shortcuts import render

# Create your views here.

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
    context = {}
    return render(request,'store/anime.html',context)

    
def web(request):
    context = {}
    return render(request,'store/web.html',context)