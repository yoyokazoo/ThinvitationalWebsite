# Generated by Django 3.1.4 on 2021-01-03 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('set_auction', '0004_auctionablesets'),
    ]

    operations = [
        migrations.AddField(
            model_name='setdraftingschedule',
            name='set_code',
            field=models.CharField(default='RIX', max_length=3),
            preserve_default=False,
        ),
    ]