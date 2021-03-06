# Generated by Django 3.1.2 on 2020-10-04 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ziponline', '0002_auto_20201004_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='goods_min_remains',
            field=models.PositiveSmallIntegerField(verbose_name='Мин. Остаток'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='goods_now_remain',
            field=models.PositiveSmallIntegerField(verbose_name='Остаток'),
        ),
        migrations.AlterField(
            model_name='moving',
            name='Moving_type',
            field=models.CharField(choices=[('move', 'Перемещение'), ('outgo', 'Расход')], max_length=12, verbose_name='Тип движения'),
        ),
        migrations.AlterField(
            model_name='moving',
            name='move_from',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='transfer_from', to='ziponline.storage', verbose_name='Откуда'),
        ),
        migrations.AlterField(
            model_name='moving',
            name='move_task',
            field=models.CharField(max_length=12, verbose_name='Задача'),
        ),
        migrations.AlterField(
            model_name='moving',
            name='move_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='transfer_to', to='ziponline.storage', verbose_name='Куда'),
        ),
        migrations.AlterField(
            model_name='storage',
            name='storage_name',
            field=models.CharField(max_length=10, verbose_name='Подрядчик'),
        ),
    ]
