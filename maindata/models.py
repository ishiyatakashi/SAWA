from django.db import models


class Category(models.Model):
    """カテゴリ"""
    name = models.CharField(max_length=255,primary_key=True)

    def __str__(self):
        return self.name


class Entertainer(models.Model):
    """芸能人"""
    id = models.IntegerField('ID', blank=True, default=0,primary_key=True )
    name = models.CharField('名前', max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
