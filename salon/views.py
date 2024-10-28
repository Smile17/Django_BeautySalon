from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "index.html")

def masters(request):
    return render(request, "masters.html")

def master(request, master_id):
    context = {'master_id': master_id}
    return render(request, "master.html", context)

def prices(request):
    return render(request, "prices.html")

def contacts(request):
    return render(request, "contact.html")