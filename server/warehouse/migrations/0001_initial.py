# Generated by Django 2.0.7 on 2019-06-03 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Pavadinimas')),
                ('category', models.CharField(max_length=100, verbose_name='Tipas')),
                ('color', models.CharField(max_length=100, verbose_name='Spalva')),
                ('condition', models.CharField(max_length=100, verbose_name='Būklė')),
                ('description', models.TextField(verbose_name='Aprašymas')),
            ],
        ),
    ]
