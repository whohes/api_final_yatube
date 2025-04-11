from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .views import (
    PostViewSet,
    CommentViewSet,
    GroupViewSet,
    FollowViewSet)


router = DefaultRouter()
router.register(r'v1/posts', PostViewSet, basename='post')
router.register(r'v1/groups', GroupViewSet, basename='group')
router.register(r'v1/follow', FollowViewSet, basename='follow')
router.register(
    r'v1/posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comment')


urlpatterns = [
    path('', include(router.urls)),
    path('v1/', include('djoser.urls.jwt')),
]
