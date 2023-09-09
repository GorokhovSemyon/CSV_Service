from django.urls import path
from . import views

urlpatterns = [
    path('csvfiles/', views.CsvFileList.as_view(), name='csvfile-list'),
]
