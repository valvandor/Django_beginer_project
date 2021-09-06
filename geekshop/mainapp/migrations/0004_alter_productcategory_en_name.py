# Generated by Django 3.2.6 on 2021-09-06 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_productcategory_en_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcategory',
            name='en_name',
            field=models.CharField(max_length=64, unique=True, verbose_name='имя категории на английском'),
        ),
    ]
