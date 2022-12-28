from django.urls import path
from nwsportal.views import PostList,PostDetail,PostCreate,PostEdit,PostDelete,SearchList, CategoryListView, subscribe


urlpatterns = [
      path('', PostList.as_view(), name = 'post_list' ),
      path('<int:pk>', PostDetail.as_view(), name = 'post_details'),
      path('search/', SearchList.as_view(), name = 'post_search'),
      path('create/', PostCreate.as_view(), name='post_create'),
      path('<int:pk>/edit/', PostEdit.as_view(), name='post_update'),
      path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
      path('categories/<int:pk>', CategoryListView.as_view(), name='category_list'),
      path('categories/<int:pk>/subscribe', subscribe, name='subscribe')
         ]
