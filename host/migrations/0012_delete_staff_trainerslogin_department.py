# Generated by Django 4.2 on 2023-06-04 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('host', '0011_trainerslogin_delete_enrollments'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Staff',
        ),
        migrations.AddField(
            model_name='trainerslogin',
            name='department',
            field=models.CharField(max_length=50, null=True),
        ),
    ]