from django.db import models

class User(models.Model):
   admission_number = models.CharField(max_length=200, unique=True)
   email = models.EmailField(unique=True)
