# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_budget_rubro'),
    ]

    operations = [
        migrations.AddField(
            model_name='parameter',
            name='attribute',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='parameter',
            name='description',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='parameter',
            name='status_parameter',
            field=models.CharField(default='', max_length=1),
            preserve_default=False,
        ),
    ]
