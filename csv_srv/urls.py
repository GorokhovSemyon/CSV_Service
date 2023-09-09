from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import CsvFileList, CsvFileViewOnly, CsvFileAPIView

router = DefaultRouter()
router.register(r'csvfiles', CsvFileViewOnly, basename='csvfile')

urlpatterns = [
    path('', views.CsvUploadView.as_view(), name='csv-upload'),
    path('api/csv_files/', CsvFileList.as_view(), name='csv-file-list'),
    path('api/', include(router.urls)),
    path('api/csv_file/<int:csv_file_id>/', CsvFileAPIView.as_view(), name='csv-view')
]
