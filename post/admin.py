from django.contrib import admin

# Register your models here.
from .models import Like, Post, Comment
# Register your models here.
admin.site.register(Like)
admin.site.register(Post)
admin.site.register(Comment)