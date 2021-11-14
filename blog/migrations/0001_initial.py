# Generated by Django 3.1.13 on 2021-11-14 13:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import easy_thumbnails.fields
import taggit.managers
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0003_taggeditem_add_unique_index'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True, verbose_name='Title')),
                ('title_de', models.CharField(max_length=200, unique=True, verbose_name='Title German')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='Slug')),
                ('slug_de', models.SlugField(max_length=200, unique=True, verbose_name='Slug German')),
                ('thumbnail', easy_thumbnails.fields.ThumbnailerImageField(blank=True, upload_to='', verbose_name='Thumbnail')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Created on')),
                ('content', tinymce.models.HTMLField(verbose_name='Content')),
                ('content_de', tinymce.models.HTMLField(verbose_name='Content German')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Author')),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]
