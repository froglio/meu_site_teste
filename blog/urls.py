from django.urls import path

from . import views

urlpatterns = [
    path('', views.BlogListView.as_view(), name='home'),
    path('post/new', views.BlogCreateView.as_view(), name='post_new'),
    path('post/<slug:slug>/<int:pk>', views.BlogDetailView.as_view(), name='post_detail'),
    path('post/<slug:slug>/<int:pk>/edit', views.BlogUpdateView.as_view(), name='post_edit'),
    path('post/<slug:slug>/<int:pk>/delete', views.BlogDeleteView.as_view(), name='post_delete'),
]