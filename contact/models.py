from django.db import models
from django.utils import timezone

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=20)

    created_date = models.DateTimeField(default=timezone.now)
