# Generated by Django 3.2 on 2021-06-25 15:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('movierater', '0008_rater_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='rater',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
