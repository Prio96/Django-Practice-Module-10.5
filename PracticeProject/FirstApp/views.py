from django.shortcuts import render

# Create your views here.
def home(request):
    d={}
    return render(request,"FirstApp/home.html",d)
