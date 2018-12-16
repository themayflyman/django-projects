from django.urls import path, include, reverse_lazy

from . import views


app_name = 'bbs'
board_patterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<str:x>/', views.BoardView.as_view(), name='board'),
    path('<str:x>/post/', views.NewPostView.as_view(success_url=reverse_lazy('bbs:index')), name='new_post'),
    path('<str:x>/<int:pk>/', views.PostView.as_view(), name='post'),
]
urlpatterns = [
    path('board/', include(board_patterns)),
]
