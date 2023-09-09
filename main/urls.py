from django.urls import path, include
from django.contrib.auth import views as auth_views
from main import views

urlpatterns = [
    path('', views.index, name='home'),
    path('devs/', views.devs, name='devs'),
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('register/', views.register, name='register'),
    path('csv_service/', include('csv_srv.urls')),
    path('REST/', include('accounts.urls')),
]
