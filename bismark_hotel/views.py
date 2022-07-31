from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Room, Contact, Booked

# Create your views here.
def index(request):
    rooms = Room.objects.all()
    return render(request, 'index.html', {'rooms': rooms})

def rooms(request):
    
    rooms = Room.objects.all()
    return render(request, 'rooms.html', {'rooms': rooms})




def contact(request):
    if request.method == 'POST':
    
        fullname = request.POST['fullname']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        message = Contact.objects.create(full_name = fullname, email = email, subject = subject, message = message)
        message =message.save();

        return redirect('index')


    else:
        return render(request, 'contact.html')





def about(request):
    return render(request, 'about.html')

def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username = username).exists():
                messages.info(request, "Username taken")
                return redirect('register')

            elif User.objects.filter(email = email).exists():
                messages.info(request, "Email taken")
                return redirect('register')
                
            else:
                user = User.objects.create_user(first_name = first_name, last_name = last_name, username = username, email = email, password = password1);
                user.save();
                return redirect('login') 

        else:
            print("Password Not Matching")
            return redirect('register')
    else:
        return render(request, 'register.html')

    


def login(request):
    if request.method == 'POST':
        username=request.POST['username'] 
        password=request.POST['password'] 

        user = auth.authenticate(username = username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.info(request,'Invalid credentials')
            return redirect('login')

    else:
        return render(request, 'login.html')







def bookroom(request, id):
    object = Room.objects.get(id=id)
    return render(request, 'bookroom.html', { 'room': object })



def roomdetails(request, id):

    object = Room.objects.get(id=id)
    #obj = Room.objects.get(id = id)
    
    return render(request, 'bookroom.html', {'object': object})
    



def logout(request):
    auth.logout(request)
    return redirect('index')


def saveroom(request, id):

    user = User.objects.get(id=id)
    #rooms = Room.objects.all()
    room = Room.objects.get()
    #object = Room.objects.get(id=id)
    #obj = Room.objects.get(id = id)

    # we're collaborating here

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        mobile_phone = request.POST['mobile_phone']
        address = request.POST['address']
        room_type = request.POST.get('room_type', '')
        state = request.POST.get('state', '')
        checkin_date = request.POST['check_in_date']
        checkout_date = request.POST['check_out_date']
        number_of_guests = int(request.POST.get('number_of_guests',''))
        number_of_rooms = int(request.POST.get('number_of_rooms', ''))
        price = request.POST.get('price', '')
        

        booked = Booked.objects.create(first_name = first_name, last_name = last_name, email = email, mobile_phone = mobile_phone, address = address, room_type = room_type, 
        state = state, checkin_date = checkin_date, checkout_date = checkout_date, number_of_guests = number_of_guests, number_of_rooms = number_of_rooms, 
        price = price)
        print(booked)

        booked = booked.save();

        return redirect('index')
    
    else:
        return render(request, 'bookroom.html', {'user': user}, {'rooms': rooms})
