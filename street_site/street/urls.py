from django.urls import path
from django.contrib.auth import views as auth_views

from street import views

urlpatterns = [
    path('', views.index, name='index'),

    path('home/', views.home, name='home'),

    path('login/', views.login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

