# Generated by Django 3.1.7 on 2021-05-28 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogAPP', '0011_user_information_aboutu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_information',
            name='AboutU',
            field=models.TextField(blank=True, max_length=200),
        ),
    ]