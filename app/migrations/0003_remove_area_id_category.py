# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_delete_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='area',
            name='id_category',
        ),
    ]
