# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_budget_id_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='area',
            name='status',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
