from django.shortcuts import render
from rest_framework.views import APIView
from .models import Post,Comment
from .serializers import PostSerializer,CommentSerializer
from rest_framework import permissions,status,generics,viewsets
from rest_framework.response import Response

from django.http import Http404
from rest_framework.generics import get_object_or_404


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer 
    queryset = Post.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class AddCommentView(APIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def post(self,request,post_id=None):
        post = Post.objects.get(pk=post_id)
        serializer = CommentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(post=post,author_comment=self.request.user)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)   

    def get(self,request,post_id=None):
        post = Post.objects.get(pk=post_id)
        serializer = CommentSerializer(post.comments,many=True)    
        return Response(serializer.data)





