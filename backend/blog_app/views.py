from .models import Post, Comment
from rest_framework import viewsets, permissions
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .seriallizers import UserSerializer, CommentSerializer, PostSerializer
from .permissions import IsOwnerOrReadOnly



class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer



class PostsViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `like` action.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    # @action(detail=True)
    # def like(self, request, *args, **kwargs):
    #     status_code = status.HTTP_200_OK
    #     snippet = self.get_object()
    #     try:
    #         snippet.like_post(request.user)
    #     except ValueError:
    #         status_code = status.HTTP_400_BAD_REQUEST
    #     return Response(snippet, status=status_code)


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)



class CommentsViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


#TODO: add 
