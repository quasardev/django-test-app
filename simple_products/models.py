from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    descr = models.TextField()
    width = models.IntegerField()
    heigth = models.IntegerField()
    color_1 = models.CharField(max_length=7)

    def __unicode__(self):
        return self.name