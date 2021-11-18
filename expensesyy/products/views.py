from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Receipt
from .forms import ProductForm, ReceiptForm


# Create your views here.
def base_view(request, *args, **kwargs):
    print(request)
    print(request.user)
    print(args)
    return render(request, "base.html", {})

#PRODUCTS
def product_view(request):
    obj = Product.objects.all()
    context = {
        'products_list': obj
    }
    return render(request, "product.html", context)


def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("main")

    context = {
        'form': form
    }
    return render(request, "product_create.html", context)


def product_update_view(request, pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(request.POST or None, instance=product)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect("main")
    context = {
        'form': form
    }
    return render(request, "product_create.html", context)


def get_custom_product_view(request, pk):
    product = get_object_or_404(Product, id=pk)
    return render(request, "specific_product.html", {'product': product})

def product_delete_view(request, pk):
    product = Product.objects.get(id=pk)
    if request.method == 'POST':
        product.delete()
        return redirect("main")
    context = {
        'obj' : product
    }
    return render(request, "delete.html", context)

#RECEIPTS
def receipt_view(request):
    obj = Receipt.objects.all()
    receipt_pk = obj[0].id
    products = Product.objects.filter(receipt__pk=receipt_pk)
    context = {
        'receipts_list': obj,
        'products': products,
        'receipt_pk': receipt_pk
    }
    return render(request, "receipt.html", context)

def receipt_create_view(request):
    form = ReceiptForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("main")

    context = {
        'form': form
    }
    return render(request, "receipt_create.html", context)

def receipt_update_view(request, pk):
    receipt = Receipt.objects.get(id=pk)
    form = ReceiptForm(request.POST or None, instance=receipt)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect("main")
    context = {
        'form': form
    }
    return render(request, "receipt_create.html", context)

def receipt_delete_view(request, pk):
    receipt = Receipt.objects.get(id=pk)
    if request.method == 'POST':
        receipt.delete()
        return redirect("main")
    context = {
        'obj' : receipt
    }
    return render(request, "delete.html", context)