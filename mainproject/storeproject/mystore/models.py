from django.db import models

# Create your models here.
class Product(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,default='')
    description = models.CharField(max_length=150)
    price=models.DecimalField('price', max_digits=9, decimal_places=2, default=0)
    stock=models.IntegerField()
    def __str__(self):
        return self.name
