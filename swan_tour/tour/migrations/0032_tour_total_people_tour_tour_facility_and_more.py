# Generated by Django 4.0.6 on 2024-03-21 10:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0031_tourfacility_tourrepeatoption_tourvehicle_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='total_people',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='tour',
            name='tour_facility',
            field=models.ManyToManyField(related_name='facilitys', to='tour.tourfacility'),
        ),
        migrations.AddField(
            model_name='tour',
            name='tour_vehicle',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tour_vehicle', to='tour.tourvehicle'),
        ),
        migrations.AlterField(
            model_name='tour',
            name='end_date',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='tour',
            name='group_size',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tour',
            name='start_date',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='tourfacility',
            name='facility',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='tourvehicle',
            name='vehicle',
            field=models.CharField(max_length=2000),
        ),
    ]
