# Generated by Django 3.1.2 on 2020-10-04 13:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ziponline', '0004_auto_20201004_1646'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='good',
            options={'ordering': ['-goods_name'], 'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.AlterModelOptions(
            name='moving',
            options={'ordering': ['-move_date'], 'verbose_name': 'Движение', 'verbose_name_plural': 'Движения'},
        ),
        migrations.AlterModelOptions(
            name='storage',
            options={'ordering': ['-storage_name'], 'verbose_name': 'Склад', 'verbose_name_plural': 'Склады'},
        ),
        migrations.AddField(
            model_name='moving',
            name='move_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Дата добавления'),
            preserve_default=False,
        ),
    ]
