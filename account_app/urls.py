from django.urls import path
import account_app.views as views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.signin, name='logout'),

]