from django.shortcuts import render, redirect
from .models import Room, Topic, Message
from .forms import RoomForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Userprofile
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, CreateView, DeleteView
from .forms import UserProfileForm
from .forms import UserProfileForm, CustomUserForm, CustomUserProfileForm, UserUpdateForm, UserRegistrationForm
from django.http import HttpResponse

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

  room = Room.objects.get(id=pk)
  
  room_messages = room.message_set.all().order_by('-created')  # query child object of a specific room , message is a model nam e
  participants = room.participants.all()
  if request.method == 'POST':
            message = Message.objects.create(
               user = request.user,
               room = room,
               body = request.POST.get('body'),
            )
            room.participants.add(request.user)
            return redirect('room', pk=room.id)
        

      
  context = {'room':room, 'room_messages':room_messages, 'participants':participants}
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

# Delete Message 
@login_required(login_url='/LoginPage/')
def delete_message(request,pk):
  messages = Message.objects.get(id=pk)
  # form = RoomForm(instance=messages)

  if request.user != messages.user:
     return HttpResponse("You aren't allowed to  delete")

  if request.method == "POST":
    messages.delete()
    return redirect('Home')
  
  context = {"message":messages}
  return render (request, 'base/delete_message.html',context)




# using CBV pattern to upload and create user profile 

class MyProfileView(LoginRequiredMixin, DetailView ):
   model = Userprofile
   template_name='my_profile.html'

   def get_object(self):
      obj, created = Userprofile.objects.get_or_create(user=self.request.user)
      return obj
   

# Create a new profile 

class UserProfileDetailView(DetailView):
   model = Userprofile
   template_name = 'base/profile_detail.html'

   def get_object(self):
      return Userprofile.objects.get(user = self.request.user)





# Update User profile 

class MyProfileUpdateView(LoginRequiredMixin,UpdateView):
   model=Userprofile
   form_class= UserProfileForm
   template_name= 'profiles/profile_form.html.html'
   success_url = reverse_lazy('profile-list')


# class ModelNameDetail(DetailView):
#     model = Userprofile
#     template_name='profiles_lazy.delay.html'
#     sucess_fuerm = reverse_lazy('group-t')

# UserProfileDeleteView 

class UserProfileDeleteView(LoginRequiredMixin,DeleteView):
   model=Userprofile
   template_name= 'profiles/profile_confirm_delete.html'
   success_url = reverse_lazy('profile-list')
   