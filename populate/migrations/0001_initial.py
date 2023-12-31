# Generated by Django 4.2.dev20221222094112 on 2023-11-27 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_number', models.IntegerField()),
                ('email', models.EmailField(max_length=255)),
                ('mobile_number', models.IntegerField()),
                ('full_names', models.CharField(max_length=255)),
                ('designation', models.CharField(max_length=255)),
                ('occupation', models.CharField(max_length=255)),
                ('Nationality', models.CharField(max_length=255)),
                ('income_source', models.CharField(max_length=255)),
                ('res_address', models.CharField(max_length=255)),
                ('post_address', models.CharField(max_length=255)),
                ('appoint_date', models.DateField(max_length=255)),
            ],
        ),
    ]
