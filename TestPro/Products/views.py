from django.shortcuts import render
from .models import ToDoList
from .forms import ProductForm
from  django.shortcuts import HttpResponse


def list_products(request):
    products = ToDoList.objects.all()

    return render(request, 'Product.html', {"products": products})


def create_product(request):
    form=ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponse("Successfully Saved in DB")
    return render(request,'product-form.html',{'form':form})
