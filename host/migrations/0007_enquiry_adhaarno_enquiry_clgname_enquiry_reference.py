# Generated by Django 4.1.6 on 2023-05-31 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('host', '0006_enquiry_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='enquiry',
            name='adhaarno',
            field=models.CharField(max_length=55, null=True),
        ),
        migrations.AddField(
            model_name='enquiry',
            name='clgname',
            field=models.CharField(max_length=55, null=True),
        ),
        migrations.AddField(
            model_name='enquiry',
            name='reference',
            field=models.CharField(max_length=55, null=True),
        ),
    ]
