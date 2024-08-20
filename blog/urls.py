from django.urls import path
from blog import views

app_name = 'blog'
urlpatterns = [
    path('blog/', views.blog, name='blog'),
    path('blog/<slug:slug>/<int:pk>/', views.blog_detail, name='blog-detail'),
]