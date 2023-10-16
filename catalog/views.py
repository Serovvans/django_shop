from django.shortcuts import render
from catalog.utils import load_contacts_to_json


# Create your views here.
def home(request):
    return render(request, 'catalog/home.html')


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        load_contacts_to_json(name, phone, message)
    return render(request, 'catalog/contacts.html')
