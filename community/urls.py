from django.urls import path
from .views import PostView ,CommentView


urlpatterns = [
    # path('', views.post_list, name='post_list'),
    # path('post/<int:pk>/', views.post_detail, name='post_detail'),
    # path('post/create/', views.post_create, name='post_create'),
    # path('post/<int:pk>/comment/', views.add_comment, name='add_comment'),
    # path('post/<int:pk>/like/', views.like_post, name='like_post'),
    path('posts/<int:post_id>/', PostView.as_view(), name='post-detail'),
    # path('comment/<int:comment_id>/delete/', views.comment_delete, name='comment_delete'),
    path('posts/',PostView.as_view(),name='post-list'),
    path('posts/<int:post_id>/comments/', CommentView.as_view(), name='comment-list'),
    path('posts/<int:post_id>/comments/<int:comment_id>/', CommentView.as_view(), name='comment-detail'),
]
