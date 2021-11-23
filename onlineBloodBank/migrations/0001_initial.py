# Generated by Django 3.2.4 on 2021-07-04 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('birth_date', models.DateField(max_length=100)),
                ('country', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('blood_group', models.CharField(max_length=10)),
                ('contact_number', models.IntegerField()),
                ('email', models.EmailField(max_length=100)),
                ('message', models.TextField(max_length=200)),
            ],
        ),
    ]
