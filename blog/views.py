from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView
from taggit.models import Tag

from .models import Article


class ArticleList(ListView):
    queryset = Article.objects.all().order_by('-created_on')
    template_name = 'posts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        common_tags = Article.tags.most_common()[:4]
        context["common_tags"] = common_tags
        return context


class ArticleDetail(DetailView):
    model = Article
    template_name = 'post.html'


class TaggedListView(ArticleList, ListView):
    view_url_name = "djangocms_blog:posts-tagged"

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(tags__slug=self.kwargs["slug"])

    def get_context_data(self, **kwargs):
        kwargs["tagged_entries"] = self.kwargs.get("slug") if "slug" in self.kwargs else None
        context = super().get_context_data(**kwargs)
        return context