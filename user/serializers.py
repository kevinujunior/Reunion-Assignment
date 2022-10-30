from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import  User,UserFollowing
from rest_framework.response import Response



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username','email']
        
        
        
class UserFollowingSerializer(serializers.ModelSerializer):
    currUser = serializers.CurrentUserDefault()
    
    class Meta:
        model = UserFollowing
        fields = ["id","followingUser",]  
    
    def create(self, validated_data):
        request = self.context.get('request', None)
        followingUser = self.validated_data['followingUser']
        if request.user!=followingUser:
            UserFollowing.objects.create(currUser = request.user, followingUser = followingUser)
       
        return UserFollowing(**validated_data)
     

class UnFollowSerializer(serializers.ModelSerializer):
    currUser = serializers.CurrentUserDefault()
    class Meta:
        model = UserFollowing
        fields = ["id", "followingUser",]  
    
    def create(self, validated_data):
        followingUser = self.validated_data['followingUser']
        request = self.context.get('request', None)
        obj = UserFollowing.objects.get(currUser = request.user, followingUser = followingUser)
        obj.delete()
        return UserFollowing(**validated_data)
 

class CustomJWTSerializer(TokenObtainPairSerializer):
    
    def validate(self, attrs):
        credentials = {
            'username': '',
            'password': attrs.get("password")
        }

        # This is answering the original question, but do whatever you need here. 
        # For example in my case I had to check a different model that stores more user info
        # But in the end, you should obtain the username to continue.
        user_obj = User.objects.filter(email=attrs.get("username")).first() or User.objects.filter(username=attrs.get("username")).first()
        if user_obj:
            credentials['username'] = user_obj.username

        return super().validate(credentials)
  


class ProfileSerializer(serializers.Serializer):
    following = serializers.SerializerMethodField()
    followers= serializers.SerializerMethodField()
    username = serializers.SerializerMethodField()
    class Meta:
        model = UserFollowing
        fields = ['username','followers','following']
    
    
    def get_username(self,obj):
        user = User.objects.get(username=obj.username)
        username = user.username
        return username
    
    def get_following(self,obj):
        following = UserFollowing.objects.filter(currUser = obj)
        return len(following)

    def get_followers(self,obj):
        follower = UserFollowing.objects.filter(followingUser = obj)
        return len(follower)
        
    