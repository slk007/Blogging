from django.urls import path

from .views import (AboutView, PostListView, PostDetailView, 
                    PostCreateView, PostUpdateView, PostDeleteView, 
                    DraftListView, add_comment_to_post, comment_approve, comment_remove, post_publish)

urlpatterns = [
    path("about/", AboutView.as_view(), name='about'),
    path('', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/remove/', PostDeleteView.as_view(), name='post_remove'),
    path('post/<int:pk>/publish/', post_publish, name='post_publish'),
    path('drafts/', DraftListView.as_view(), name='post_draft_list'),
    path('post/<int:pk>/comment/', add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/approve/', comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', comment_remove, name='comment_remove'),
]