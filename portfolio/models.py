from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)    
    description = models.CharField(max_length=500)
    img_alt = models.CharField(max_length=100)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)
    texturl = models.CharField(max_length=100)    
    

    def __str__(self):
        return self.title