# Generated by Django 5.1.4 on 2025-01-04 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_ingredients'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Recipe',
        ),
    ]
