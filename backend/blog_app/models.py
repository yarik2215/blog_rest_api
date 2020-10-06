from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import ManyToManyField
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
from django.utils.translation import gettext_lazy as _

from django.utils.text import slugify  


class Post(models.Model):
    '''
    Post model. Store post text, owner etc.
    '''
    title = models.CharField(_('title'), max_length=200)
    slug = models.SlugField(max_length=255, db_index=True, unique=False)
    owner = models.ForeignKey(get_user_model(), on_delete=CASCADE, verbose_name=_('owner'))
    likes = models.ManyToManyField(get_user_model(), related_name='liked_posts')
    text = models.TextField()
    updated = models.DateTimeField(_('updated'), auto_now=True)

    def save(self, *args, **kwargs) -> None:
        '''
        Prepopuldate slug with post title and post id last 50 digits.
        '''
        self.slug = slugify(' '.join(self.owner.username[0:50], self.title))
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        '''
        Return slug.
        '''
        return self.slug

    def count_likes(self) -> int:
        '''
        Count likes for post.
        '''
        return self.likes.count()

    def like_post(self, user) -> None:
        '''
        Recieve user instance that want to like post.
        If user alreday like that post raise ValueError,
        else add user to self.likes .
        '''
        if user in self.likes:
            raise ValueError(f'User already have liked this post.')
        self.likes.add(user)



class Comment(models.Model):
    '''
    Comment model. Refers on post and owner (user). 
    '''
    post = ForeignKey('Post', on_delete=CASCADE, verbose_name=_('post'))
    owner = ForeignKey(get_user_model(), on_delete=CASCADE, verbose_name=_('owner'))
    text = models.TextField()
    updated = models.DateTimeField(_('updated'), auto_now=True)
