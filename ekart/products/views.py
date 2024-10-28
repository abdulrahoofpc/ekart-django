from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    featured_priorty=Product.objects.order_by('priorty')[:4]
    Latest_priorty=Product.objects.order_by('-priorty')[:4]
    context={'featured_priorty':featured_priorty,
             'Latest_priorty':Latest_priorty}
    print(context)
    return render(request,'index.html',context)

def product(request,pk):
    product=Product.objects.get(pk=pk)
    context={'product': product }
    return render(request,'product_details.html',context)

def list(request):
    """_summary_ """


    page=1
    if request.GET:
        page=request.GET.get('page',1)
    product_list=Product.objects.order_by('priorty')
    product_paginator=Paginator(product_list,4)
    product_list=product_paginator.get_page(page)
    context={
        'products':product_list
    }
    return render(request,'products.html',context)
