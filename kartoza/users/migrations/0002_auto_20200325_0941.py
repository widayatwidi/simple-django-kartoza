# Generated by Django 2.2.11 on 2020-03-25 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='profile.png', upload_to='profile_pics'),
        ),
    ]
