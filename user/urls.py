from django.urls import path, include

from rest_framework.routers import DefaultRouter
from post.views import AllPostViewSet

from user.views import (
   UserFollowingViewSet,
   UnfollowViewSet,
   ProfileViewSet,
)

        
        
router = DefaultRouter()
router.register("all_posts", AllPostViewSet, basename="all-post-view")
#router.register("unfollow", UnfollowViewSet, basename="user-unfollow-view")
router.register("user", ProfileViewSet, basename="user-profile-view")

urlpatterns = [
    path("", include(router.urls)),
]
