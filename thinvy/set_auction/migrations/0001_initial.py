# Generated by Django 3.1.4 on 2020-12-31 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SetDraftingSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('set_name', models.CharField(max_length=100)),
                ('end_time', models.DateField()),
            ],
        ),
    ]
