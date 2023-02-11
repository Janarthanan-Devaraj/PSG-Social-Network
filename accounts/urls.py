from django.urls import path

from . import views

urlpatterns = [
    path('signup/', views.signupPage, name="signup"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('',views.home, name="home")
]