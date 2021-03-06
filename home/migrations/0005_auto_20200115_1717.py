# Generated by Django 2.2.7 on 2020-01-15 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20200111_0435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='time_from',
            field=models.DateTimeField(verbose_name='Дата отправления и время'),
        ),
        migrations.AlterField(
            model_name='order',
            name='time_return_transfer',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Время обратного трансфера'),
        ),
    ]
