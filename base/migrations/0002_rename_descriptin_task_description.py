# Generated by Django 5.1.1 on 2024-09-28 07:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='descriptin',
            new_name='description',
        ),
    ]
