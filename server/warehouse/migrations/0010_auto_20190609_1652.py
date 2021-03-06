# Generated by Django 2.0.7 on 2019-06-09 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0009_auto_20190608_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='condition',
            field=models.IntegerField(choices=[(1, 'Puiki'), (2, 'Labai gera'), (3, 'Gera'), (4, 'Prasta'), (5, 'Labai prasta'), (6, 'Netinkama naudoti'), (7, 'Nėra')], default=7, verbose_name='Būklė'),
        ),
        migrations.AlterField(
            model_name='item',
            name='state',
            field=models.IntegerField(choices=[(1, 'Laisva'), (2, 'Rezervuota'), (3, 'Paimta')], default=1, verbose_name='Statusas'),
        ),
    ]
