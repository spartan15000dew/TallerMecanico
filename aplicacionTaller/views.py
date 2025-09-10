from django.shortcuts import render

# Create your views here.
def rendertemplate(request):
    return render(request,"aplicacionTaller/login.html")

def rendermMenu(request):
    return render(request,"aplicacionTaller/menu.html")