from rest_framework import generics
from .models import CsvFile
from .serializers import CsvFileSerializer

class CsvFileList(generics.ListCreateAPIView):
    queryset = CsvFile.objects.all()
    serializer_class = CsvFileSerializer
