from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, CommentCreateView


app_name = 'blog'


urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('new/', PostCreateView.as_view(), name='post_create'),
    path('<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('<int:pk>/comment/', CommentCreateView.as_view(), name='comment_create'),
]


