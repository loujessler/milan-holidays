# Generated by Django 2.2.7 on 2020-01-11 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_remove_status_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='chair_large',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='15-36 кг'),
        ),
        migrations.AddField(
            model_name='order',
            name='chair_middle',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='9-18 кг'),
        ),
        migrations.AddField(
            model_name='order',
            name='chair_small',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='0-13 кг'),
        ),
        migrations.AddField(
            model_name='order',
            name='children_passenger',
            field=models.IntegerField(blank=True, null=True, verbose_name='Кол-во детей'),
        ),
    ]
