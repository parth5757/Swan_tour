# Generated by Django 4.0.6 on 2024-02-19 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='group_size',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tour',
            name='total_price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
