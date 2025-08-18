from django.shortcuts import render, redirect
from .models import Room, Topic
from .forms import RoomForm


# Create your views here.

# demo file 

# rooms = [
# {  'id':1, 'name':'python'},
#   {'id':2, 'name':'Django'},
#   {'id':3, 'name':'Javascript'},
# ]

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


def delete_Room(request,pk):
  room = Room.objects.get(id=pk)
  form = RoomForm(instance=room)

  if request.method == "POST":
    room.delete()
    return redirect('Home')
  
  context = {"form":form}
  return render (request, 'base/delete_room.html',context)

