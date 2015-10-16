# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_valueparameter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='description',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='budget',
            name='description',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='rubro',
            name='description',
            field=models.CharField(max_length=255, blank=True),
        ),
    ]
