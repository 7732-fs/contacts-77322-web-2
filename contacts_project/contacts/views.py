from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.http import JsonResponse
from django.core import serializers

from django.shortcuts import render, redirect
from .models import Contact

import contacts.functions as functions
from .forms import ContactForm, ContactFormFromModel

@login_required(login_url="/login")
def home(request):
    return render(request, "contacts/index.html", {"form":ContactFormFromModel(), "contacts":Contact.objects.all()})

def api(request):
    return JsonResponse(serializers.serialize("json", Contact.objects.all()), safe=False)

def num(request):
    return JsonResponse({"num":len(Contact.objects.all())})

def my_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(f"/")
        else:
            raise PermissionDenied()
    # request.session['next'] = request.GET.get("next", "/")
    return render(request, 'contacts/login.html')

def add(request):
    name=request.GET["name"]
    phone=request.GET["phone"]
    #functions.add(request.GET)
    f=ContactFormFromModel(request.GET)
    if f.is_valid():
        ContactFormFromModel(request.GET).save()
    else:
        return render(request=request, template_name="contacts/error.html")
    return redirect('home')

def view(request):
    return str(functions.view())

def delete(request):
    name=request.args["name"]
    functions.delete(name)
    return redirect('home')

def update(request):
    if request.method=='POST':
        c=Contact.objects.get(request.GET["id"])
        ContactFormFromModel(request.GET, instance=c).save()
        return redirect('home')
    else:
        c=Contact.objects.get(pk=request.GET["id"])
        return render(request, "contacts/update.html", {"form":ContactFormFromModel(request.GET, instance=c)})