# Generated by Django 4.2 on 2023-06-12 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('host', '0014_attendence'),
    ]

    operations = [
        migrations.CreateModel(
            name='ToDO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=55)),
                ('date', models.DateField()),
                ('description', models.CharField(max_length=55)),
            ],
            options={
                'db_table': 'todo',
            },
        ),
    ]
