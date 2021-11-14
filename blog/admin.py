from django.contrib import admin

from blog.models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_on', 'tags')
    list_filter = ("tags",)
    search_fields = ['title', 'content', 'tags']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Article, ArticleAdmin)
