# Generated by Django 4.1.4 on 2023-07-27 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instituteapp', '0005_rename_frist_name_contactdata_first_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='registerData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('Password', models.BigIntegerField(max_length=100)),
            ],
        ),
    ]
