# Generated by Django 4.1.6 on 2023-05-27 08:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('host', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='courses',
            old_name='courseName',
            new_name='coursename',
        ),
    ]
