from django.apps import AppConfig


class BlogConfig(AppConfig):
    label = 'blog'
    verbose_name = 'Django Divio Blog'
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
