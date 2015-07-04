# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patent', '0004_auto_20150704_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patentapplication',
            name='australian_appl_no',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]
