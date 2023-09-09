from rest_framework import generics
from .models import CsvFile
from .serializers import CsvFileSerializer
from django.shortcuts import render
from django.views import View
from .forms import CsvUploadForm
import pandas as pd

class CsvFileList(generics.ListCreateAPIView):
    queryset = CsvFile.objects.all()
    serializer_class = CsvFileSerializer

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
                # Если файл пустой, обработайте это
                return render(request, self.template_name, {'form': form, 'error_message': 'Empty file!'})

            # Создаем экземпляр модели CsvFile и сохраняем его в базе данных
            csv_file_instance = CsvFile(
                name=uploaded_file.name,
                columns=list(df.columns),  # Записываем имена колонок в виде списка
            )
            csv_file_instance.save()

            # После успешной обработки, вы можете перенаправить пользователя или отобразить сообщение об успехе
            return render(request, self.template_name, {'form': form, 'success_message': 'File uploaded successfully!'})

        # Если форма не валидна, отобразите ошибки
        return render(request, self.template_name, {'form': form})