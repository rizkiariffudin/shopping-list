from django.shortcuts import render
from django.http import HttpResponseRedirect
from main.forms import ProductForm
from django.urls import reverse
from main.forms import Product
from django.http import HttpResponse
from django.core import serializers

from django.shortcuts import get_object_or_404
from main.models import Product  # Replace 'myapp' and 'YourModel' with your actual app and model names

def delete_xml_data(request, pk):
    # Get the object you want to delete
    obj = get_object_or_404(Product, pk=pk)

    # Perform the deletion
    obj.delete()

    return HttpResponse("Data deleted successfully")

# Create your views here.
def show_main(request):
    products = Product.objects.all()

    context = {
        'name': 'Rizki Ariffudin', # Nama kamu
        'class': 'PBP E', # Kelas PBP kamu
        'products': products
    }

    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")