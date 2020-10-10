# Generated by Django 3.1.2 on 2020-10-10 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ziponline', '0007_auto_20201004_1728'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='moving',
            options={'ordering': ['-pk'], 'verbose_name': 'Движение', 'verbose_name_plural': 'Движения'},
        ),
        migrations.AddField(
            model_name='storage',
            name='storage_description',
            field=models.CharField(max_length=150, null=True, verbose_name='Описание'),
        ),
    ]
