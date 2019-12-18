from django.db import models


class Genre(models.Model):
    """ジャンル"""
    name = models.CharField('大分類', max_length=255)
    publisher = models.CharField('小分類', max_length=255, blank=True)
    page = models.IntegerField('ジャンル名前', blank=True, default=0)

    def __str__(self):
        return self.name
