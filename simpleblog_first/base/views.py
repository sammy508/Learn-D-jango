from django.shortcuts import render, redirect
from .models import Room, Topic
from .forms import RoomForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm




# Create your views here.

# demo file 

# rooms = [
# {  'id':1, 'name':'python'},
#   {'id':2, 'name':'Django'},
#   {'id':3, 'name':'Javascript'},
# ]


def LoginPage(request):
  if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('Home')
        else:
            messages.error(request, "Invalid username or password")
            return render(request, 'base/login-template.html', {'username': username})
        return render(request, 'base/login-template.html')

  return render(request, 'base/login-template.html')

# have to update field validations and change email to username format on login form 


# Error : 
# def userRegestration_Form(request):
#   form = UserCreationForm()
#   if request.method == 'POST':
#     form = UserCreationForm(request.POST)
#     if form.is_valid():
#       try:
#         form.save()
#         messages.success(request, "Registration successful. Please log in.")
#         return redirect('LoginPage')
#       except Exception as e:
#         messages.error(request,"Invalid data. Please try again.")
    
      

#   return render (request,'base/regestration-template.html', {'form':form})


def userRegistration_Form(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Registration successful. Please log in.")
                return redirect('LoginPage')
            except Exception as e:
                messages.error(request, f"Error: {str(e)}")
        else:
            messages.error(request, "Invalid data. Please try again.")
    else:
        form = UserCreationForm()

    return render(request, 'base/regestration-template.html', {"form": form})



# To make a Logout buttton 
def Logoutbutton(request):
      logout(request)
      return redirect('LoginPage')

# To restrict page and make login required we have to import login required library and implement login required decorators 

def Home(request):

  q = request.GET.get('q') if request.GET.get('q')!=None else ''
  rooms = Room.objects.filter(topic__name__icontains=q) # Jun jun topic ma search text hunxa tyo show garxa 
  topics = Topic.objects.all()
  context = {'rooms':rooms, 'topics':topics}
  
  return  render (request, 'base/home.html', context)  # now we can pass that rooms dictionary data to home page and can access  // put single braces otherwise you get error

def Rooms(request,pk):

  room  = Room.objects.all()
  for i in room: 
    if i.id == int(pk): 
      room = i
      
  context = {'room':room}
  return  render (request, 'base/room.html', context)


# CRUD OPeration 
@login_required(login_url='/LoginPage/')  # Login required restrict user access those pages without registration 
def Create_Room(request):
  form = RoomForm()

  if request.method == 'POST':
    form = RoomForm(request.POST)
    print(request.POST)

    if form.is_valid():
      form.save()
      return redirect('Home')


  context = {'form':form}
  return render (request, 'base/room_form.html', context)

# UPdate Room


@login_required(login_url='/LoginPage/')
def update_Room(request, pk):
  room = Room.objects.get(id=pk)
  form = RoomForm(instance=room)
 

  if request.method == 'POST':
     form = RoomForm(request.POST, instance=room)

  if form.is_valid():
    form.save()
    return redirect('Home')
  
  context = {'form':form}

  return render (request, 'base/room_form.html',context)

# Delete Room 

@login_required(login_url='/LoginPage/')
def delete_Room(request,pk):
  room = Room.objects.get(id=pk)
  form = RoomForm(instance=room)

  if request.method == "POST":
    room.delete()
    return redirect('Home')
  
  context = {"form":form}
  return render (request, 'base/delete_room.html',context)

# have to add later if user is already logged in then prevent user from login again 

