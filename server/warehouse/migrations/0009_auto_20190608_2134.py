# Generated by Django 2.2.2 on 2019-06-08 21:34

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('warehouse', '0008_auto_20190608_1622'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 6, 8, 21, 34, 34, 853774, tzinfo=utc), verbose_name='Data'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='state',
            field=models.IntegerField(choices=[(1, 'Laisva'), (2, 'Rezervuota'), (3, 'Paimta')], default=1),
        ),
        migrations.AddField(
            model_name='item',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='ItemState',
        ),
    ]
