# Generated by Django 4.2 on 2023-06-19 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('host', '0015_todo'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendence',
            name='email',
            field=models.CharField(max_length=55, null=True),
        ),
        migrations.AlterField(
            model_name='attendence',
            name='date',
            field=models.CharField(max_length=55, null=True),
        ),
        migrations.AlterField(
            model_name='attendence',
            name='name',
            field=models.CharField(max_length=55, null=True),
        ),
        migrations.AlterField(
            model_name='attendence',
            name='roll_no',
            field=models.CharField(max_length=55, null=True),
        ),
        migrations.AlterField(
            model_name='attendence',
            name='status',
            field=models.CharField(max_length=55, null=True),
        ),
    ]