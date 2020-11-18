from django.db import models


# Create your models here.
class PRModel(models.Model):
    pr_num = models.PositiveIntegerField(verbose_name='номер ПР', primary_key=True)
    pr_text = models.CharField(verbose_name='Temporary field', max_length=30)

    def __str__(self):
        return str('Задание номер ' + str(self.pr_num))

    class Meta:
        verbose_name_plural = "Проблемы"
        verbose_name = "Проблема"
        ordering = ['pr_num']
