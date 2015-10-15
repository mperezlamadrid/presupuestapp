# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_area_id_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='budget',
            name='id_category',
        ),
    ]
