# Generated by Django 2.0 on 2018-01-12 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basketR', '0003_auto_20171218_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='pNum',
            field=models.IntegerField(),
        ),
    ]
