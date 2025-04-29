from django.db import models
from datetime import date

# Create your models here.

# makemigrations - create changes and store in a file
# migrate - apply the pending changes created by makemigrations

class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=13)
    desc = models.TextField()
    date = models.DateField(default=date.today)  # Added date field to store submission date

    def __str__(self):
        return self.name  # This makes it easier to identify records in Django Admin
