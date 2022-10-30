"""reuinion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include,re_path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    
)
from post.views import CommentViewSet, LikeViewSet, UnLikeViewSet

from user.views import(
    UnfollowViewSet,
    UserFollowingViewSet,
)

from user.serializers import(
    CustomJWTSerializer,
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('user.urls')),
    path('api/authenticate/', TokenObtainPairView.as_view(serializer_class=CustomJWTSerializer), name='token_obtain_pair'),
    path('api/token/refresh/',TokenRefreshView.as_view(),name = 'token_refresh'),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('api-auth/', include('rest_framework.urls')), 
    path('api/', include('post.urls')),
    path("api/unfollow/<int:pk>", UnfollowViewSet.as_view(), name="unfollow-user"),
    path("api/follow/<int:pk>", UserFollowingViewSet.as_view(), name="unfollow-user"),
    path("api/like/<int:pk>", LikeViewSet.as_view(), name="like-post"),
    path("api/unlike/<int:pk>", UnLikeViewSet.as_view(), name="unlike-post"),
    path("api/comment/<int:pk>", CommentViewSet.as_view(), name="comment-post"),
]
