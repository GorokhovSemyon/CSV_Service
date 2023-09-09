from django.urls import path
from . import views

urlpatterns = [
    path('', views.CsvUploadView.as_view(), name='csv-upload'),
]
