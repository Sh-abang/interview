from django.db import models

# Create your models here.
from django.db import models

class CustUsers(models.Model):
    id_number = models.IntegerField()
    email = models.EmailField(max_length=255)
    mobile_number = models.IntegerField()
    full_names = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    occupation = models.CharField(max_length=255)
    Nationality = models.CharField(max_length=255)
    income_source = models.CharField(max_length=255)
    res_address = models.CharField(max_length=255)
    post_address = models.CharField(max_length=255)
    appoint_date = models.DateField()

