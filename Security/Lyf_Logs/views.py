from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "index.html")

def add(request):
    return HttpResponse("You're adding a new log entry.")

def delete(request, id):
    return HttpResponse(f"You're deleting log entry {id}.")

def edit(request, id):
    return HttpResponse(f"You're editing log entry {id}.")

def view(request, id):
    return HttpResponse(f"You're viewing log entry {id}.")

