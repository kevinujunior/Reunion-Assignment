from rest_framework import serializers
from .models import  Post, Like,Comment
from rest_framework.response import Response


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id','title', 'description','createdAt']
        


class LikeViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['post','user']  
    
    def create(self, validated_data):
        request = self.context.get('request', None)
        post = self.validated_data['post']
        if len(Like.objects.filter(user = request.user, post = post))==0:
            obj = Like.objects.create(user = request.user, post = post)
        return Like(**validated_data)
    

class UnLikeViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['post','user']  
    
    def create(self, validated_data):
        request = self.context.get('request', None)
        post = self.validated_data['post']
        obj = Like.objects.get(user = request.user, post = post)
        obj.delete()
        return Like(**validated_data)
    
    
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id','post','comment','user']
    
    def create(self, validated_data):
        request = self.context.get('request', None)
        post = self.validated_data['post']
        comment = self.validated_data['comment']
        
        return Comment(**validated_data)

class CommentForPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['comment',] 
    
class AllPostSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()
    likes = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = ['id','title', 'description','createdAt', 'comments', 'likes']
        
    
    def get_comments(self,obj):
        comments = Comment.objects.filter(post=obj)
        return CommentForPostSerializer(comments, many=True).data
        
    def get_likes(self,obj):
        likes = Like.objects.filter(post=obj)
        return len(likes)