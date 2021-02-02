from django.db import models

class Plant(models.Model):
    img_alt = models.CharField(max_length=100)
    image = models.ImageField(upload_to='portfolio/images/')

    def __str__(self):
        return self.img_alt