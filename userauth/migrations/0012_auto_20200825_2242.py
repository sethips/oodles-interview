# Generated by Django 3.1 on 2020-08-25 22:42

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0011_auto_20200825_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=phone_field.models.PhoneField(max_length=255, unique=True),
        ),
    ]
