# Generated by Django 2.2.19 on 2021-04-14 23:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='loadfile',
            name='summary',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='loadfile',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
