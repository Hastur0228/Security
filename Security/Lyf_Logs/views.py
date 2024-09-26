from django.shortcuts import render
from django.http import HttpResponse
from .models import LyfLogs

# Create your views here.
def lyf(request):
    latest_lyf_list = LyfLogs.objects.order_by("-created_at")[:5]
    context = {"latest_lyf_list": latest_lyf_list}
    return render(request, "lyf.html", context)

def add(request):
    return HttpResponse("You're adding a new log entry.")

def delete(request, id):
    return HttpResponse(f"You're deleting log entry {id}.")

def edit(request, id):
    return HttpResponse(f"You're editing log entry {id}.")

def view(request, id):
    return HttpResponse(f"You're viewing log entry {id}.")

