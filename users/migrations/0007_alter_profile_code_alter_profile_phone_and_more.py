# Generated by Django 4.0 on 2022-11-24 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_profile_auth_token_profile_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='code',
            field=models.CharField(default='', max_length=3),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='profile',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]
