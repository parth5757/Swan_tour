# Generated by Django 5.0.2 on 2024-03-09 13:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0019_rename_tour_type_tourtype'),
    ]

    operations = [
        migrations.CreateModel(
            name='TourImage',
            fields=[
                ('id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to='image/tour/image')),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tour.tour')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
