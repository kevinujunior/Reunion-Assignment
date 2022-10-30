from winreg import REG_OPTION_BACKUP_RESTORE
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from post.views import (
   PostCreateViewSet
)

router = DefaultRouter()
router.register("posts", PostCreateViewSet, basename="post-view")


urlpatterns = [
    path("", include(router.urls)),
]
