# Generated by Django 4.2 on 2023-06-04 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('host', '0010_enquiry_department_enquiry_course_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trainerslogin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'Trainers_login_table',
            },
        ),
        migrations.DeleteModel(
            name='Enrollments',
        ),
    ]
