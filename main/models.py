from django.db import models

# Create your models here.

class TestModel(models.Model):
  test_string = models.CharField(max_length=50)
  test_number = models.IntegerField()
