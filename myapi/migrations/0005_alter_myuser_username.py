# Generated by Django 4.1.7 on 2023-07-16 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0004_alter_myuser_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='username',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]