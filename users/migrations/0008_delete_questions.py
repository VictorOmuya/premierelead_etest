# Generated by Django 4.0 on 2022-11-25 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_profile_code_alter_profile_phone_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Questions',
        ),
    ]
