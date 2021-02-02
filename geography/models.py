from django.db import models

class Landscape(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    img_alt = models.CharField(max_length=100)
    image = models.ImageField(upload_to='portfolio/images/')


    def __str__(self):
        return self.title    
# Create your models here.
