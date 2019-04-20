from django.urls import path
import blog_app.views as views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('blog-all/', views.blog_all),
    path('<int:blog_id>/', views.blog_detail),
]