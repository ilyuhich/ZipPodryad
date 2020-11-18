from django.db import models


# Create your models here.

class TMCRashod(models.Model):
    """оставляю в работе нужно сначал создать сущность ПР"""
    pass
    '''goods_name = models.CharField(max_length=70, verbose_name='Наименование', unique=True)

    class Meta:
        verbose_name_plural = "Товары"
        verbose_name = "Товар"
        ordering = ['-goods_name']

    def __str__(self):
        return str(self.goods_name)'''
