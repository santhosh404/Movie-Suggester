# Generated by Django 3.2 on 2021-05-25 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movierater', '0005_remove_rater_userid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rater',
            name='Added_At',
        ),
        migrations.AddField(
            model_name='rater',
            name='Rating',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default=5, max_length=10),
            preserve_default=False,
        ),
    ]