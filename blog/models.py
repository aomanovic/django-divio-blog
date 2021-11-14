from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext as _
from easy_thumbnails.fields import ThumbnailerImageField
from taggit.managers import TaggableManager
from tinymce.models import HTMLField


class Article(models.Model):
    title = models.CharField(max_length=200, unique=True, verbose_name=_('Title'))
    title_de = models.CharField(max_length=200, unique=True, verbose_name=_('Title German'))
    slug = models.SlugField(max_length=200, unique=True, verbose_name=_('Slug'))
    slug_de = models.SlugField(max_length=200, unique=True, verbose_name=_('Slug German'))
    thumbnail = ThumbnailerImageField(blank=True, verbose_name=_('Thumbnail'))
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('Author'))
    created_on = models.DateTimeField(auto_now_add=True, verbose_name=_('Created on'))
    content = HTMLField(verbose_name=_('Content'))
    content_de = HTMLField(verbose_name=_('Content German'))
    tags = TaggableManager(verbose_name=_('Tags'))

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
