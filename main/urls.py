from django.urls import path, include
from django.contrib.auth import views as auth_views
from main import views

urlpatterns = [
    path('', views.index, name='home'),
    path('devs/', views.devs, name='devs'),
    path('about/', views.about, name='about'),
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('register/', views.register, name='register'),
    path('REST/', include('accounts.urls')),
]
