# Generated by Django 3.1.2 on 2020-11-01 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PRModel',
            fields=[
                ('pr_num', models.PositiveIntegerField(primary_key=True, serialize=False, verbose_name='номер ПР')),
                ('pr_text', models.CharField(max_length=30, verbose_name='Temporery field')),
            ],
        ),
    ]
