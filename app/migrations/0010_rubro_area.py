# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20151016_1514'),
    ]

    operations = [
        migrations.AddField(
            model_name='rubro',
            name='area',
            field=models.ForeignKey(default=1, to='app.Area'),
        ),
    ]
