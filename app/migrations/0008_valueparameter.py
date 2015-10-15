# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20151015_2136'),
    ]

    operations = [
        migrations.CreateModel(
            name='ValueParameter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.CharField(max_length=30)),
                ('order', models.CharField(max_length=3)),
                ('status_value_parameter', models.CharField(max_length=1)),
                ('parameter', models.ForeignKey(to='app.Parameter')),
            ],
        ),
    ]
