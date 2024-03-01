from django.db import models

class Hoodie(models.Model):
    name = models.CharField(max_length=100)
    details = models.TextField(max_length=300)
    category = models.CharField(max_length=10)
    size = models.CharField(max_length=10)
    color = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    avaiable = models.BooleanField(default=True)
    # image

    def __str__(self):
        return self.name