# Generated by Django 4.0.6 on 2024-02-27 06:39

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0011_alter_tour_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='tour_slug',
            field=autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='name', unique=True),
        ),
    ]