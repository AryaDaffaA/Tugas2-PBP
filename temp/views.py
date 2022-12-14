from django.shortcuts import render
from todolist.models import TodoList
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from todolist.forms import addNewTask

# TODO: Create your views here.
@login_required(login_url='/todolist/login/')
def todoList(request):
    data_todoList = TodoList.objects.filter(user = request.user)
    context = {
        'todoList': data_todoList,
        'nama': 'Arya Daffa',
        'NPM': '2106650853',
        
    }  
    return render(request, "todolist.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:todoList")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

def add_task(request):

    if request.method == "POST":
        form = addNewTask(request.POST)
        if form.is_valid():
            data = TodoList(
                user = request.user,
                date = datetime.datetime.now(),
                title = form.cleaned_data('Judul'),
                description = form.cleaned_data('Deskripsi')
            )
            data.save()
            return redirect('todolist:todoList')
    
    form = addNewTask()
    context = {'form':form}
    return render(request, 'addTask.html', context)