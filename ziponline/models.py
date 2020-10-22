from django.db import models
from django.utils.timezone import now


# Create your models here.

class Sklad(models.Model):
    good = models.ForeignKey('Good', on_delete=models.PROTECT)
    sklA_num = models.PositiveSmallIntegerField(verbose_name='Ария', default=0)
    sklA_num_app = models.PositiveSmallIntegerField(verbose_name='Ария по актам', default=0)
    sklA_num_min = models.PositiveSmallIntegerField(verbose_name='Ария мин.', default=0)
    sklB_num = models.PositiveSmallIntegerField(verbose_name='Б+', default=0)
    sklB_num_app = models.PositiveSmallIntegerField(verbose_name='Базис+ по актам', default=0)
    sklB_num_min = models.PositiveSmallIntegerField(verbose_name='Б+ мин.', default=0)
    sklAU_num = models.PositiveSmallIntegerField(verbose_name='АиЮ', default=0)
    sklAU_num_app = models.PositiveSmallIntegerField(verbose_name='АиЮ по актам', default=0)
    sklAU_num_min = models.PositiveSmallIntegerField(verbose_name='АиЮ мин.', default=0)
    sklSt_num = models.PositiveSmallIntegerField(verbose_name='Старт', default=0)
    sklSt_num_app = models.PositiveSmallIntegerField(verbose_name='Старт по актам', default=0)
    sklSt_num_min = models.PositiveSmallIntegerField(verbose_name='Старт мин.', default=0)

    class Meta:
        verbose_name_plural = "Товары на складах"
        verbose_name = "Товар на складах"
        ordering = ['-good']

    def __str__(self):
        return str(self.good)


# модель СКЛАД - хранятся только названия склада. Добавить склад ПР/НРД
class Storage(models.Model):
    storage_name = models.CharField(max_length=10, verbose_name='Подрядчик')
    storage_description = models.CharField(max_length=150, verbose_name='Описание', default='Добавьте описание')

    # goods_name = models.ForeignKey('Good', on_delete=models.PROTECT, null=True)

    class Meta:
        verbose_name_plural = "Склады"
        verbose_name = "Склад"
        ordering = ['-storage_name']

    def __str__(self):
        return str(self.storage_name)


#  создаем модель товаров на складе
class Good(models.Model):
    goods_name = models.CharField(max_length=70, verbose_name='Наименование', unique=True)

    class Meta:
        verbose_name_plural = "Товары"
        verbose_name = "Товар"
        ordering = ['-goods_name']

    def __str__(self):
        return str(self.goods_name)


#  модель Транзакция - может либо между складами либо расход
class Moving(models.Model):
    Moving_type = models.CharField(max_length=12, verbose_name='Тип движения',
                                   choices=(
                                       ('move', 'Перемещение'),
                                       ('outgo', 'Расход'),
                                   ))
    move_good = models.ForeignKey(Good,
                                  on_delete=models.PROTECT,
                                  related_name='transfer_good',
                                  verbose_name='Товар',
                                  default=1)
    move_from = models.ForeignKey(Storage,
                                  on_delete=models.PROTECT,
                                  related_name='transfer_from',
                                  verbose_name='Откуда')
    move_to = models.ForeignKey(Storage, on_delete=models.PROTECT,
                                related_name='transfer_to',
                                verbose_name='Куда')  # если под ПР/НРД указываем этот склад
    move_task = models.CharField(max_length=12,
                                 verbose_name='Задача')  # если перемещаем под ПР/НРД указываем номер
    move_date = models.DateTimeField(verbose_name='Дата добавления', default=now)

    class Meta:
        verbose_name_plural = "Движения"
        verbose_name = "Движение"
        ordering = ['-pk']

    def __str__(self):
        return '№ ' + str(self.pk)  # потом бы еще добавить дату в название
