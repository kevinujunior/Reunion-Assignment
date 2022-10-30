from rest_framework import serializers, viewsets
from user.serializers import UnFollowSerializer, UserSerializer, ProfileSerializer
from .models import UserFollowing
from user.serializers import UserFollowingSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from django.contrib.auth.models import User

class UserViewSet(viewsets.ModelViewSet):
    http_method_names = ['get']
    serializer_class = UserSerializer
    queryset = User.objects.all()
    
"""
class UserFollowingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = UserFollowingSerializer
    queryset = UserFollowing.objects.all()
    def get_queryset(self):
        try:
            queryset = UserFollowing.objects.all() 
            user = self.request.user
            if self.request.query_params.get("followingUser", None):
                followingUser = self.request.query_params.get("followingUser", None)
                queryset = queryset.filter(currUser=user, followingUser = followingUser)  
            return queryset
        except:
            return None
        
        
    def create(self, request, *args, **kwargs):
        user = self.request.user
        if self.request.query_params.get("id", None):
            followingUser = self.request.query_params.get("id", None)
            followingUser = User.objects.get(id =followingUser)
            response = "You Started Following " + followingUser.username
            if followingUser != user:
                UserFollowing.objects.create(currUser=user, followingUser = followingUser)
            else:
                return Response("Cannot follow yourself")
            return Response(response)
        else:
            return Response("You are not following this user")
   
 """   
    
class ProfileViewSet(viewsets.ModelViewSet):
    # http_method_names = ['get']
    serializer_class = ProfileSerializer
    def get_queryset(self):
        user = self.request.user
        queryset = User.objects.filter(id=user.id)
        return queryset
    
    

"""
class UnfollowViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = UnFollowSerializer
    queryset = UserFollowing.objects.all()
        
    def create(self, request, *args, **kwargs):
        user = self.request.user
        if self.kwargs.get('pk'):
            followingUser = self.kwargs.get('pk')
            # followingUser = self.request.query_params.get("id", None)
            obj = UserFollowing.objects.get(
                currUser=user, followingUser=followingUser)
            response = obj.followingUser.username + "  Unfollowed"
            obj.delete()
            return Response(response)
        else:
            return Response("You are not following this user")
    
"""    
    
"""
    def create(self, request, *args, **kwargs):
        user = self.request.user
        if self.request.query_params.get("id", None):
            followingUser = self.request.query_params.get("id", None)
            obj = UserFollowing.objects.get(currUser=user, followingUser = followingUser)
            response = obj.followingUser.username + "  Unfollowed"
            obj.delete()
            return Response(response)
        else:
            return Response("You are not following this user")
"""   
    

class UserFollowingViewSet(generics.CreateAPIView):
    serializer_class = UserFollowingSerializer
    queryset = UserFollowing.objects.all()

    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        kwargs["context"] = self.get_serializer_context()
        
        # Check if a pk was passed through the url.
        if 'pk' in self.kwargs:        
            modified_data = self.request.data.copy()
            modified_data['followingUser'] = self.kwargs.get('pk')
            modified_data['currUser'] = self.request.user.id
            kwargs["data"] = modified_data
            return serializer_class(*args, **kwargs)

        # If not mind, move on.
        return serializer_class(*args, **kwargs)
    
    
    
class UnfollowViewSet(generics.CreateAPIView):
    serializer_class = UnFollowSerializer
    queryset = UserFollowing.objects.all()

    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        kwargs["context"] = self.get_serializer_context()
        
        # Check if a pk was passed through the url.
        if 'pk' in self.kwargs:        
            modified_data = self.request.data.copy()
            modified_data['followingUser'] = self.kwargs.get('pk')
            modified_data['currUser'] = self.request.user.id
            kwargs["data"] = modified_data
            return serializer_class(*args, **kwargs)

        # If not mind, move on.
        return serializer_class(*args, **kwargs)


