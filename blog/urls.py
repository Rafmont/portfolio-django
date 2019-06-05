from django.urls import path
from . import views

urlpatterns = [
    path('blog', views.blog, name='hello'),
    path('sobre', views.sobre, name='sobre'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]
