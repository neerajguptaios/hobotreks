from django.db import models
from django.conf import settings

class VendorDetail(models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    description = models.TextField(max_length=200, null = True, blank = True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name