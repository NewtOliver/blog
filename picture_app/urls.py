from django.urls import path
import picture_app.views as views

urlpatterns = [

    path('', views.pictures, name='图集'),
    path('<int:picture_id>/', views.picture_detail),

]