from rest_framework import generics, viewsets
from .models import CsvFile
from .serializers import CsvFileSerializer
from django.shortcuts import render
from django.views import View
from .forms import CsvUploadForm
import pandas as pd
import io
from .permissions import IsAdmin
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponseServerError

class CsvFileList(generics.ListCreateAPIView):
    queryset = CsvFile.objects.all()
    serializer_class = CsvFileSerializer
    permission_classes = [IsAdmin]

class CsvFileViewOnly(viewsets.ReadOnlyModelViewSet):
    queryset = CsvFile.objects.all()
    serializer_class = CsvFileSerializer
    permission_classes = [IsAuthenticated]


class CsvFileAPIView(APIView):
    def get(self, request, csv_file_id):
        try:
            csv_data = CsvFile.objects.get(id=csv_file_id)
        except CsvFile.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        # Прочитайте файл CSV и преобразуйте его в DataFrame с помощью pandas
        try:
            csv_file = csv_data.csv_data  # Предположим, что поле csvfile ссылается на файл CSV
            df = pd.read_csv(io.StringIO(csv_file.read().decode('utf-8')))
        except Exception as e:
            return HttpResponseServerError(f"Failed to read CSV file: {e}", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # Преобразуйте DataFrame в список словарей для сериализации в JSON
        csv_rows = df.to_dict(orient='records')

        # Возвращаем данные в формате JSON
        data = {
            'name': csv_data.name,
            'columns': list(df.columns),
            'rows': csv_rows,
        }
        return Response(data, status=status.HTTP_200_OK)


class CsvUploadView(View):
    template_name = 'csv_srv/csv_upload.html'

    def get(self, request):
        form = CsvUploadForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = CsvUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Получаем загруженный файл
            uploaded_file = form.cleaned_data['csv_file']

            # Считываем содержимое CSV-файла с помощью pandas
            try:
                df = pd.read_csv(uploaded_file)
            except pd.errors.EmptyDataError:
                # Если файл пустой, это зафиксируется
                return render(request, self.template_name, {'form': form, 'error_message': 'Empty file!'})

            # Создаем экземпляр модели CsvFile и сохраняем его в базе данных
            csv_file_instance = CsvFile(
                name=uploaded_file.name,
                columns=list(df.columns),  # Записываем имена колонок в виде списка
                csv_data=uploaded_file
            )
            csv_file_instance.save()

            return render(request, self.template_name, {'form': form, 'success_message': 'File uploaded successfully!'})

        # Если форма не валидна, кинуть ошибку
        return render(request, self.template_name, {'form': form})
