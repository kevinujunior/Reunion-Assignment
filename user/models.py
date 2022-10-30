from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User

class UserFollowing(models.Model):
    currUser = models.ForeignKey(User, related_name="following", on_delete=models.CASCADE, default=None)
    followingUser = models.ForeignKey(User, related_name="followers", on_delete=models.CASCADE, default=None)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['currUser', 'followingUser'], name='unique followers')
        ]
    
    def __str__(self):
        return f"{self.currUser} follows {self.followingUser}"
    