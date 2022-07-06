# Generated by Django 3.2.14 on 2022-07-06 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('emp_id', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=150)),
                ('working', models.BooleanField(default=True)),
                ('department', models.CharField(max_length=10)),
            ],
        ),
    ]
