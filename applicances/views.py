from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def tv(request):
    return HttpResponse('<h1>The availables brands of tv are MARQ,PHILIPS,SAMSUNG,SONY,MI</h1>')
def ac(request):
    return HttpResponse('<h1>The available Air conditioners are PREMIUM ACs,SPLIT ACs,WINDOW ACs</h1>')

