# Generated by Django 3.1.7 on 2021-05-26 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogAPP', '0006_auto_20210526_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='Comment',
            field=models.TextField(max_length=2000, null=True),
        ),
    ]
