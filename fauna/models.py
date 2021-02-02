from django.db import models

class Creature(models.Model):
    title = models.CharField(max_length=100)    
    img_alt = models.CharField(max_length=100)
    image = models.ImageField(upload_to='portfolio/images/')
    
    

    def __str__(self):
        return self.title