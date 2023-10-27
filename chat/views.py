# chat/views.py
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth import login
from .models import Room, Message
from django.contrib.auth.decorators import login_required
from .forms import KayitFormu











@login_required(login_url="/login/")
def index(request):
    users =User.objects.all().exclude(username=request.user)


    return render(request, "chat/index.html" ,{"users":users})

@login_required(login_url="/login/")
def room(request, room_name):
    users =User.objects.all().exclude(username=request.user)
    room= Room.objects.get(id=room_name)
    messages = Message.objects.filter(room=room)




    return render(request, 'chat/wp.html', {'room_name': room_name,'room':room,'users':users , "messages":messages})

@login_required(login_url="/login/")
def start_chat(request,username):
    second_user = User.objects.get(username=username)
    try:
        room = Room.objects.get(first_user=request.user,second_user=second_user)
    except Room.DoesNotExist:
        try:
            room = Room.objects.get(second_user=request.user,first_user=second_user)
        except Room.DoesNotExist:
            room = Room.objects.create(first_user=request.user,second_user=second_user)
    return redirect("room", room_name=room.id)

def kayit(request):
    if request.method == "POST":
        form = KayitFormu(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Kullanıcıyı oturum açık olarak işaretle
            return redirect("/login")  # Kayıt başarılıysa ana sayfaya yönlendir
    else:
        form = KayitFormu()
    
    return render(request, "chat/register.html", {"form": form})





    

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            return render(request, "chat/login.html", {"error_message": "Kullanıcı adı veya şifre hatalı."})
    return render(request, "chat/login.html")



