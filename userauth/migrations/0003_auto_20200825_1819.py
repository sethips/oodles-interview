# Generated by Django 3.1 on 2020-08-25 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0001_initial'),
        ('userauth', '0002_auto_20200825_1818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='permanent_address',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='permanent_address', to='utils.address'),
        ),
    ]