from . import views
from django.urls import path


app_name = "blog"
urlpatterns = [
    path('', views.ArticleList.as_view(), name='posts'),
    path('<slug:slug>/', views.ArticleDetail.as_view(), name='post'),
    path('tag/<slug:slug>/', views.TaggedListView.as_view(), name="tagged"),
]