from rest_framework import generics
from .models import CsvFile
from .serializers import CsvFileSerializer
from django.shortcuts import render
from django.views import View
from .forms import CsvUploadForm

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
            # Обрабатывайте файл здесь, например, сохраняйте его в базу данных или выполняйте другие действия
            uploaded_file = form.cleaned_data['csv_file']
            # Ваша логика обработки файла

            # После успешной обработки, вы можете перенаправить пользователя или отобразить сообщение об успехе
            return render(request, self.template_name, {'form': form, 'success_message': 'File uploaded successfully!'})

        # Если форма не валидна, отобразите ошибки
        return render(request, self.template_name, {'form': form})
