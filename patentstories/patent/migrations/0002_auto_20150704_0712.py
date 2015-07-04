# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patent', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patentapplication',
            name='id',
        ),
        migrations.AlterField(
            model_name='patentapplication',
            name='australian_appl_no',
            field=models.IntegerField(serialize=False, primary_key=True),
        ),
    ]
