from django.contrib.auth.decorators import user_passes_test
from django.urls import path
from accounts import views
from accounts.views import is_staff_user

urlpatterns = [
    path('API/', user_passes_test(is_staff_user)(views.UserCreateView.as_view()), name='register_api'),
    # переход на страничку .../accounts/API (показывает POST запрос)
    path('ALL/', user_passes_test(is_staff_user)(views.UsersListView.as_view()), name='register_all'),
    # переход на страничку .../accounts/ALL (показывает всех пользователей)
    path('RUD/<int:pk>/', user_passes_test(is_staff_user)(views.UserDetailView.as_view()), name='register_rud'),
    # переход на страничку .../accounts/RUD/<номер записи> (показывает n-го пользователя)
]
