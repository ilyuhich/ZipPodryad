from django.db import models
from django.utils.timezone import now

# Create your models here.

# Модель 'Хранилище' - что хранится и на каком складе
class Warehouse(models.Model):
    storage = models.ForeignKey('Storage', on_delete=models.PROTECT)
    good = models.ForeignKey('Good', on_delete=models.PROTECT, null=True)
    remains = models.PositiveSmallIntegerField(verbose_name='Остаток', default=0)
    good_min_remains = models.PositiveSmallIntegerField(verbose_name='Мин. Остаток', default=0)

    class Meta:
        verbose_name_plural = "Хранилища (склад+товар)"
        verbose_name = "Хранилище"
        ordering = ['-storage']

    def __str__(self):
        return str(self.storage) + ' - ' + str(self.good) + ', мин. остаток ' + str(self.good_min_remains)


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
        return self.storage_name


#  создаем модель товаров на складе
class Good(models.Model):
    goods_name = models.CharField(max_length=70, verbose_name='Наименование', unique=True)
    # наименование должно быть уникальным

    # остатки должны быть привязаны не к товару, а к складу
    #    goods_min_remains = models.PositiveSmallIntegerField(verbose_name='Мин. Остаток')
    #    goods_now_remain = models.PositiveSmallIntegerField(verbose_name='Остаток')

    class Meta:
        verbose_name_plural = "Товары"
        verbose_name = "Товар"
        ordering = ['-goods_name']

    def __str__(self):
        return self.goods_name



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
