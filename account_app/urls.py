from django.urls import path
import account_app.views as views

urlpatterns = [
    path('signin/', views.signin, name='登陆'),
    path('signup/', views.signup, name='注册'),
]