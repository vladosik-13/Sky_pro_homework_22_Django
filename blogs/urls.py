from django.urls import path
from blogs.apps import BlogsConfig

from blogs.views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView

app_name = BlogsConfig.name

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('article/<int:pk>/', BlogDetailView.as_view(), name='article_detail'),
    path('article/create/', BlogCreateView.as_view(), name='article_create'),
    path('article/<int:pk>/update/', BlogUpdateView.as_view(), name='article_update'),
    path('article/<int:pk>/delete/', BlogDeleteView.as_view(), name='article_delete'),
]