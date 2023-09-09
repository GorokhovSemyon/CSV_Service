from django.db import models


class CsvFile(models.Model):
    name = models.CharField(max_length=255)
    upload_date = models.DateTimeField(auto_now_add=True)
    columns = models.JSONField()

    def __str__(self):
        return self.name
