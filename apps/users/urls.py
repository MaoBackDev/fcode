from django.urls import path

from . import views

app_name = "users"

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.UserRegisterView.as_view(),name='register'),
    path('login/', views.login_view,name='login'),
    path('logout/', views.LogoutView.as_view(),name='logout'),
    # path('profile/', views.profile,name='profile'),
]