from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def kitchen(request):
    return HttpResponse('<h1>COOKWARE,CHOPPERS,KNIFES,OUTDOOR COOKING,CHICKEN TOOLS are available</h1>')
def gardening(request):
    return HttpResponse('<h1>SOIL MANURE,PLANT SEEDS,POTS&PALNTERS,PALNT&PLANTERS,GARDEN TOOL SET,WATERING EQUIPMENT..are available</h1>')
