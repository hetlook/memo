from django.db import models

# Create your models here.


class Banner(models.Model):
    title = models.CharField(max_length=50, default='HELLO WANG')
    def __str__(self):
        return self.title


class Item(models.Model):
    name = models.CharField(max_length=20)
    url = models.URLField()
    col = models.ForeignKey('Col', on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Col(models.Model):
    title = models.CharField(max_length=50, default='列表1')
    footer = models.ForeignKey('Footer', on_delete=models.CASCADE)
    def __str__(self):
        return self.title


class Footer(models.Model):
    title = models.CharField(max_length=50, default='footer1')
    def __str__(self):
        return self.title