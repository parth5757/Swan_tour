# Generated by Django 4.0.6 on 2024-03-01 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0014_tour_booking_email_tour_booking_phone_number_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tour_booking',
            old_name='valid_date_from',
            new_name='end_date',
        ),
        migrations.RenameField(
            model_name='tour_booking',
            old_name='valid_date_till',
            new_name='start_date',
        ),
    ]