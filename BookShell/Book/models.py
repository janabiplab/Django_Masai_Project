from django.db import models

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=50)
    publish_date=models.CharField(max_length=10)
    isbn=models.IntegerField()
    price=models.DecimalField(decimal_places=2,max_digits=140000)
    stock=models.IntegerField()

    def __str__(self):
        return self.title
