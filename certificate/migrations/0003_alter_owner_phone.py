# Generated by Django 4.2.3 on 2024-03-26 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificate', '0002_alter_owner_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
