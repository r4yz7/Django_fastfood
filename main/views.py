from django.shortcuts import render, redirect
from .models import Product
from django.db.models import Value, CharField
from .forms import ProductForm, PhotoForm


def index(request):
    search = request.GET.get('search', '')
    products = Product.objects.filter(productName__icontains=search).annotate(description_list=Value('', CharField()))
    for product in products:
        product.description_list = product.description.split(',')
    context = {'products': products}
    return render(request, 'main/index.html', context)


def addProduct(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        photo_form = PhotoForm(request.POST, request.FILES)  

        if form.is_valid() and photo_form.is_valid():
            product = form.save()
            photo = photo_form.save(commit=False)
            photo.product = product
            photo.save()

            return redirect('home')
    else:
        form = ProductForm()
        photo_form = PhotoForm() 

    context = {'form': form, 'photo_form': photo_form}
    return render(request, 'main/addProduct.html', context)
