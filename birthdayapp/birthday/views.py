from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import BirthdayForm

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. Welcome to Birthdays!")

def birthday_signup(request):
    if request.method == "POST":
        form = BirthdayForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("success")
    else:
        form = BirthdayForm()
    return render(request, "birthday/signup.html", {"form": form})

def success(request):
    return render(request, 'birthdays/success.html')

