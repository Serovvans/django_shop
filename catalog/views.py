from django.shortcuts import render
from catalog.utils import load_contacts_to_json
from catalog.models import Product


def home(request):
    context = {
        "object_list": Product.objects.all(),
        "title": 'Skystore - home'
    }
    return render(request, 'catalog/home.html', context)


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        load_contacts_to_json(name, phone, message)
    return render(request, 'catalog/contacts.html')


def item(request, pk):
    context = {
        'object': Product.objects.get(pk=pk),
        'title': 'Skystore - страница товара'
    }
    return render(request, 'catalog/item.html', context)
