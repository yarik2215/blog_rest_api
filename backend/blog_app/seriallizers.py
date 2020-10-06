from rest_framework import serializers
from rest_framework import fields
from django.contrib.auth import get_user_model
from .models import Post, Comment


class PostSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.HyperlinkedRelatedField(view_name='user-detail', read_only=True)

    class Meta:
        model = Post
        fields = ['url', 'title', 'owner', 'updated', 'count_likes', 'text']



class CommentSerializer(serializers.HyperlinkedModelSerializer):
    post = serializers.HyperlinkedRelatedField(view_name='post-detail', read_only=True)
    owner = serializers.HyperlinkedRelatedField(view_name='user-detail', read_only=True)

    class Meta:
        model = Comment
        fields = ['url', 'owner', 'updated', 'text']



class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = get_user_model()
        fields = ['url', 'id', 'username', 'posts']