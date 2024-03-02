from django.db import models

class Hoodie(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200)
    details = models.TextField(max_length=300,
                               blank=True)
    size = models.CharField(max_length=10)
    color = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, 
                                decimal_places=2)
    avaiable = models.BooleanField(default=True)
    quantity = models.IntegerField(default=1)
    image = models.ImageField(upload_to='products/',
                              blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name