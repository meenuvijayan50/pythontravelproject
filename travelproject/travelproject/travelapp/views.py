from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
# Create your views here.
def demo(request):
    obj1=Place.objects.all()

    return render(request,"index.html",{'result':obj1})
#def addition(request):
 #   x=int(request.GET['num1'])
  #  y=int(request.GET['num1'])
   # res=x+y

    #return render(request,"result.html",{'result':res})
