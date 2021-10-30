from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length = 200)
    author = models.ForeignKey('Author', on_delete = models.CASCADE)
    body = models.TextField()
    createAdd = models.DateTimeField(auto_created = True)

    def __str__(self):
        return self.title

class Author(models.Model):
    fio = models.CharField(max_length = 100)
    rating = models.IntegerField()
    tag = models.CharField(max_length = 200)

    def __str__(self):
        return self.fio

