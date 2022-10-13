from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from todolist.models import Task

@login_required(login_url = "/todolist/login/")
def show_todolist(request):
    context = {
        "username": request.user
    }
    return render(request, "todolist.html", context)

def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect("todolist:show_todolist")
        else:
            messages.info(request, "Username dan password salah.")
    context = {}
    return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    return redirect("todolist:login_user")

def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Akun berhasil dibuat.")
            return redirect("todolist:login_user")
    context = {"form": form}
    return render(request, "register.html", context)

@login_required(login_url = "/todolist/login/")
def create_task(request):
    if request.method == "POST":
        judul = request.POST.get("judul")
        deskripsi = request.POST.get("deskripsi")
        Task.objects.create(user = request.user, date = timezone.now(), title = judul, description = deskripsi)
        return redirect("todolist:show_todolist")
    return render(request, "create-task.html")

@login_required(login_url = "/todolist/login/")
def show_json(request):
    data = Task.objects.filter(user = request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@login_required(login_url = "/todolist/login/")
def add_task(request):
    if request.method == "POST":
        tanggal = timezone.now()
        judul = request.POST.get("judul")
        deskripsi = request.POST.get("deskripsi")
        curTask = Task.objects.create(user = request.user, date = tanggal, title = judul, description = deskripsi)
        context = {
            "pk": curTask.id,
            "fields": {
                "date": tanggal,
                "title": judul,
                "description": deskripsi
            }
        }
        return JsonResponse(context)