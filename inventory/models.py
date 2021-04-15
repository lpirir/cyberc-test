from django.db import models
from django.utils import timezone

class Inventory(models.Model):
    serie = models.CharField(max_length=200)
    number_elements = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=9, decimal_places=2)

class LoadFile(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(default=timezone.now)
    file = models.FileField(upload_to="files")
    summary = models.CharField(max_length=250, null=True)
    
    def __str__(self):
        return self.name