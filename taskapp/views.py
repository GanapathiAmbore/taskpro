from django.shortcuts import render
from taskapp.models import Post
from taskapp.serializers import PostSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

def home(request):
    posts = Post.objects.all()
    return render(request,'home.html',{'posts':posts})
@api_view(['GET'])
def post_api(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts,many=True)
    return Response(serializer.data)
