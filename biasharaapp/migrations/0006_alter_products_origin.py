# Generated by Django 4.2.7 on 2023-11-09 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biasharaapp', '0005_products_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='origin',
            field=models.CharField(default='Kenya', max_length=50),
        ),
    ]
