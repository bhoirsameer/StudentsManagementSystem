# Generated by Django 4.2 on 2023-06-03 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('host', '0009_enrollments_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='enquiry',
            name='Department',
            field=models.CharField(max_length=55, null=True),
        ),
        migrations.AddField(
            model_name='enquiry',
            name='course',
            field=models.CharField(default='Not Enroll Yet', max_length=55),
        ),
        migrations.AddField(
            model_name='enquiry',
            name='enrl_status',
            field=models.CharField(default='NO', max_length=55),
        ),
        migrations.AddField(
            model_name='enrollments',
            name='Department',
            field=models.CharField(max_length=55, null=True),
        ),
        migrations.AlterModelTable(
            name='enrollments',
            table='enrollments',
        ),
    ]
