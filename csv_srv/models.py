from django.db import models

def default_csv():
    from django.core.files.base import ContentFile
    return ContentFile(b'', name='default.csv')

class CsvFile(models.Model):
    name = models.CharField(max_length=255)
    upload_date = models.DateTimeField(auto_now_add=True)
    columns = models.JSONField()
    csv_data = models.FileField(upload_to='csv_files/', default=default_csv)  # Specify a default value function

    def __str__(self):
        return self.name