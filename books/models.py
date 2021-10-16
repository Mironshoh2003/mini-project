from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200,verbose_name='Kitobni nomi')
    subtitle = models.CharField(max_length=200, verbose_name="Kitobni subtitle")
    author = models.CharField(max_length=200,verbose_name="Kitobni aftori")
    isbn = models.CharField(max_length=13)


    def __str__(self):
        return self.title