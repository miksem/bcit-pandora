from django.db import models

class Vendor(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    

    def __str__(self):
        return self.title    
# Create your models here.
