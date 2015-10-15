# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_area_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='budget',
            name='rubro',
            field=models.ManyToManyField(to='app.Rubro'),
        ),
    ]
