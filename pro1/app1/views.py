from django.shortcuts import render,get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from . models import Post,Comment
from . serializers import PostSerializer,CommentSerializer
# Create your views here.

class PostViewset(viewsets.ModelViewSet):
    def create(self,request):
        serializer=PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(data=serializer.errors)

    def list(self,request):
        objs=Post.objects.all()
        serializer=PostSerializer(objs,many=True)
        return Response(data=serializer.data)

    def retrieve(self,request,pk=None):
        obj=get_object_or_404(Post,id=pk)
        serializer=PostSerializer(obj)
        return Response(data=serializer.data)
    
    def update(self,request,pk=None):
        obj=get_object_or_404(Post,id=pk)
        serializer=PostSerializer(instance=obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(data=serializer.errors)
    
    def partial_update(self,request,pk=None):
        obj=get_object_or_404(Post,id=pk)
        serializer=PostSerializer(instance=obj,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(data=serializer.errors)
    
    def destroy(self,request,pk=None):
        obj=get_object_or_404(Post,id=pk)
        obj.delete()
        return Response(data={"msg":'DATA DELETED SUCCESSFULY'})
    
class CommentViewset(viewsets.ModelViewSet):
    serializer_class=CommentSerializer
    queryset=Comment.objects.all()