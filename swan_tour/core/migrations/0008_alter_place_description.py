    # Generated by Django 4.0.6 on 2024-03-21 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_city_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='description',
            field=models.TextField(max_length=1000),
        ),
    ]
