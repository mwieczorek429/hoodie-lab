from django.db import models

class Size(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Hoodie(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200)
    details = models.TextField(max_length=300,
                               blank=True)
    color = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, 
                                decimal_places=2)
    image = models.ImageField(upload_to='products/',
                              blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
    

class HoodieSize(models.Model):
    hoodie = models.ForeignKey(Hoodie,
                               on_delete=models.CASCADE)
    size = models.ForeignKey(Size,
                             on_delete=models.CASCADE)
    stock = models.IntegerField(default=0)   
    available = models.BooleanField(default=False) 

    def __str__(self):
        return f'{self.hoodie.name} | Size: {self.size.name} | Stock: {self.stock}'