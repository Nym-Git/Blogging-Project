# Generated by Django 3.1.7 on 2021-05-24 18:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('BlogAPP', '0002_auto_20210524_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_information',
            name='User_Name',
            field=models.OneToOneField(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]