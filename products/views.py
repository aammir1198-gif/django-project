from django.shortcuts import render

from products.models import Products

from django.http import JsonResponse

from products.forms import ProductFormModel

from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt

def show_products(request):

    if request.method == "GET":

        return JsonResponse (list(Products.objects.all().values()) , safe=False)
    
    elif request.method == "POST":

        form = ProductFormModel(request.POST)

        if form.is_valid():

            form.save()

            return JsonResponse({'status' : 'its okey'})
        
        return JsonResponse({'status' : 'its not okey'})