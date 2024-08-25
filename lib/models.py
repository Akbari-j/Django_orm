from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    publish_date = models.DateField()
    isbn = models.CharField(max_length=13)
    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    def __str__(self):
        return self.name