from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def womenethinic(request):
    return HttpResponse('<h1>SAREES,KURTAS,SALWAR,GOWNS,LEHANGAS are available</h1>')
def womenfootwear(request):
    return HttpResponse('<h1>FLATS,HEELS,WEDGES,SHOE,SANDALS are available</h1>')

