# Generated by Django 5.0.2 on 2024-03-17 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0028_tour_included'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='image_2',
            field=models.ImageField(blank=True, null=True, upload_to='image/tour/'),
        ),
        migrations.AlterField(
            model_name='tour',
            name='image_3',
            field=models.ImageField(blank=True, null=True, upload_to='image/tour/'),
        ),
        migrations.AlterField(
            model_name='tour',
            name='tour_image',
            field=models.ImageField(blank=True, null=True, upload_to='image/tour/'),
        ),
        migrations.AlterField(
            model_name='tourhistoryvisit',
            name='visit',
            field=models.BooleanField(default=False),
        ),
    ]
