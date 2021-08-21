from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from . models import Product

def product_list(request):
    products=Product.objects.all()
    #return HttpResponse(products)
    return render(request,'products/productslist.html',{'productos':products})


