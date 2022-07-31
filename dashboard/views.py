from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from bismark_hotel.models import Contact, Room


# Create your views here.
def users(request):
    users = User.objects.all()
    return render(request, 'users.html', {'users': users})

def bookings(request):
    return render(request, 'bookings.html')

def room(request):
    rooms = Room.objects.all()
    return render(request, 'room.html', {'rooms': rooms})

def messages(request):
    messages = Contact.objects.all()
    return render(request, 'messages.html', {'messages': messages})

def edit(request, id):
    user = User.objects.get(id=id)
    return render(request, 'edit.html', {'user': user})

def update(request, id):

    user = User.objects.get(id=id)
    #user = User.objects.all()

    if request.method == 'POST':
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.username = request.POST['username']
        user.email = request.POST['email']
        user.is_staff = request.POST['is_staff']
        user.is_staff = False
        
        user = user.save();
        
        return redirect('users')
        
    else:
         return render(request, 'index.html', {'user': user})


def delete(request, id):
    user = User.objects.filter(id=id)
    user.delete()
    return render(request, 'users.html', {'user': user})

def delete(request, id):
    room = Room.objects.filter(id=id)
    room.delete()
    return render(request, 'room.html', {'room': room})