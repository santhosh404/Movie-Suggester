# Generated by Django 3.2 on 2021-05-24 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movierater', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rater',
            name='Description',
            field=models.TextField(),
        ),
    ]