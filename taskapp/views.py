from django.shortcuts import render
from taskapp.models import Post

def home(request):
    posts = Post.objects.all()
    return render(request,'home.html',{'posts':posts})