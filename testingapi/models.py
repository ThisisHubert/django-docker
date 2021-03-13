from django.db import models

# Create your models here.


class Members(models.Model):
    fullname = models.CharField(max_length=100)
    mem_code = models.CharField(max_length=3)
    title = models.CharField(max_length=10)
    phone_number = models.IntegerField(max_length=11)
    job_desc = models.CharField(max_length=100)
    
    
