# Generated by Django 5.0.6 on 2024-05-22 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_menu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='status',
            field=models.IntegerField(choices=[(1, 'Available'), (0, 'Unavailable')], default=1),
        ),
    ]