# Generated by Django 4.1.7 on 2023-07-18 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0006_alter_myuser_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsersMatching',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user1_email', models.EmailField(max_length=254)),
                ('user2_email', models.EmailField(max_length=254)),
            ],
        ),
    ]