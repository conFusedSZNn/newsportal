from django.urls import path
from .views import PostList, PostDetail, PostCreate,PostEdit,PostDelete, PostartCreate,PostartEdit,PostartDelete


urlpatterns = [
   path('', PostList.as_view(), name = 'post_list' ),
   path('<int:pk>', PostDetail.as_view(), name = 'post_details'),
   path('search/', PostList.as_view(), name = 'post_search'),
   path('create/', PostCreate.as_view(), name='post_create'),
   path('<int:pk>/edit/', PostEdit.as_view(), name='post_update'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path('create/', PostartCreate.as_view(), name='postart_create'),
   path('<int:pk>/edit/', PostartEdit.as_view(), name='postart_update'),
   path('<int:pk>/delete/', PostartDelete.as_view(), name='postart_delete'),
]
