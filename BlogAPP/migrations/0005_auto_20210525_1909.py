# Generated by Django 3.1.7 on 2021-05-25 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogAPP', '0004_instruction_liked_int_m'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instruction',
            name='Liked_int_M',
            field=models.IntegerField(default='0', max_length=100),
        ),
    ]
