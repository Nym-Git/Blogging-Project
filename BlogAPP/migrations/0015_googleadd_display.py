# Generated by Django 3.1.7 on 2021-05-28 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogAPP', '0014_auto_20210528_1854'),
    ]

    operations = [
        migrations.AddField(
            model_name='googleadd',
            name='Display',
            field=models.BooleanField(default=True),
        ),
    ]