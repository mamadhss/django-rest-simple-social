from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('posts',views.PostViewSet)
app_name = 'blogapi'

urlpatterns = [
    #path('posts/', views.PostList.as_view()),
    #path('posts/<int:pk>/', views.PostDetail.as_view()),
    #path('posts/<int:pk>/comment', views.AddComment.as_view(), name='comment'),
    path('',include(router.urls)),
    path('posts/<int:post_id>/comment/',views.AddCommentView.as_view()),
    #path('posts/comment/<int:comment_id>/',views.ManageCommentView.as_view())


]

