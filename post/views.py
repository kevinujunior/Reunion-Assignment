from logging import raiseExceptions
from django.http import Http404
from rest_framework import viewsets
from post.serializers import PostSerializer, LikeViewSerializer, UnLikeViewSerializer, CommentSerializer, AllPostSerializer
from .models import Post, Like, Comment
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from django.core.exceptions import ValidationError
from django.core.exceptions import BadRequest

# Create your views here.


class PostCreateViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
  
    
    def get_queryset(self):
        user = self.request.user
        post = Post.objects.filter(user = user)
        return post
    
    def create(self, request, *args, **kwargs):
        
        serializer = PostSerializer(data=request.data)
        user = self.request.user
        if serializer.is_valid():
            title = serializer.validated_data['title']
            description = serializer.validated_data['description']
            post = Post.objects.create(user = user, title=title, description = description)
            return Response({'id':post.id ,
                             'title':post.title,
                             'description':post.description,
                             'Created At':post.createdAt},status=201
                            ) 
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    
    

class LikeViewSet(generics.CreateAPIView):
    serializer_class = LikeViewSerializer
    queryset = Like.objects.all()

    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        kwargs["context"] = self.get_serializer_context()
        # Check if a pk was passed through the url.
        if 'pk' in self.kwargs:        
            modified_data = self.request.data.copy()
            modified_data['post'] = self.kwargs.get('pk')
            modified_data['user'] = self.request.user.id
            kwargs["data"] = modified_data
            
            return serializer_class(*args, **kwargs)

        # If not mind, move on.
        return serializer_class(*args, **kwargs
                                )
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
            
        
        
class UnLikeViewSet(generics.CreateAPIView):
    serializer_class = UnLikeViewSerializer
    queryset = Like.objects.all()

    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        kwargs["context"] = self.get_serializer_context()
        # Check if a pk was passed through the url.
        if 'pk' in self.kwargs:        
            modified_data = self.request.data.copy()
            modified_data['post'] = self.kwargs.get('pk')
            modified_data['user'] = self.request.user.id
            kwargs["data"] = modified_data
            return serializer_class(*args, **kwargs)

        # If not mind, move on.
        return serializer_class(*args, **kwargs)
    


class CommentViewSet(generics.CreateAPIView, generics.RetrieveAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        kwargs["context"] = self.get_serializer_context()
        # Check if a pk was passed through the url.
        if 'pk' in self.kwargs:        
            modified_data = self.request.data.copy()
            modified_data['post'] = self.kwargs.get('pk')
            modified_data['user'] = self.request.user.id
            kwargs["data"] = modified_data
            return serializer_class(*args, **kwargs)

        # If not mind, move on.
        return serializer_class(*args, **kwargs)
    
    def create(self, request, *args, **kwargs):
        data = request.data
        user = self.request.user
        post = Post.objects.get(id=self.kwargs.get('pk'))
        if(data['comment']==''):
            return Response('Invalid request.', status.HTTP_400_BAD_REQUEST)
        obj = Comment.objects.create(user=user,post = post, comment = data)
             
        return Response({'id':obj.id})
        
        



class AllPostViewSet(viewsets.ModelViewSet):
    serializer_class = AllPostSerializer
    
    def get_queryset(self):
        user = self.request.user
        post = Post.objects.filter(user = user)
        return post