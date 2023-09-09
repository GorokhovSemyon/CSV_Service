from django.urls import path
from . import views
from .views import CsvFileList

urlpatterns = [
    path('', views.CsvUploadView.as_view(), name='csv-upload'),
    path('api/csv_files/', CsvFileList.as_view(), name='csv-file-list'),
]
