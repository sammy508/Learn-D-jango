from django.shortcuts import render

# Create your views here.

# demo file 

rooms = [
{  'id':1, 'name':'python'},
  {'id':2, 'name':'Django'},
  {'id':3, 'name':'Javascript'},
]

def Home(request):
  
  return  render (request, 'base/home.html', {'rooms':rooms})  # now we can pass that rooms dictionary data to home page and can access  // put single braces otherwise you get error

def Room(request,pk):

  room = None
  for i in rooms: 
    if i ['id'] == int(pk):
      room = i
  context = {'room':room}
  return  render (request, 'base/room.html', context)