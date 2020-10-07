from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'posts', views.PostsViewSet)
router.register(r'comments', views.CommentsViewSet)
router.register(r'users', views.UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
]