# Generated by Django 3.2.9 on 2023-05-09 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proapp', '0002_bookingform'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingform',
            name='email',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='bookingform',
            name='name',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='bookingform',
            name='phone',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='bookingform',
            name='select',
            field=models.CharField(max_length=10),
        ),
    ]