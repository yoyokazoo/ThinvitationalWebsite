# Generated by Django 3.1.4 on 2020-12-31 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('set_auction', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setdraftingschedule',
            name='end_time',
            field=models.DateField(null=True),
        ),
    ]
