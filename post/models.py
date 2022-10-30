from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(User,on_delete = CASCADE)
    title = models.TextField(null=False)
    description = models.TextField(null = False)
    createdAt = models.DateTimeField(auto_now_add=True)
    
    
class Like(models.Model):
    post = models.ForeignKey("post.Post", related_name="likedonpost",on_delete=CASCADE)
    user = models.ForeignKey(User,related_name="likeby", on_delete = CASCADE)
    

    def __str__(self):
        return f"{self.post} liked by {self.user}"
    
    


class Comment(models.Model):
    comment = models.TextField(null=False)
    user = models.ForeignKey(User,related_name="commentby", on_delete = CASCADE)
    post = models.ForeignKey("post.Post", related_name="commentonpost",on_delete=CASCADE)

    def __str__(self):
        return f"{self.id} - commented by {self.user}"
    
    
