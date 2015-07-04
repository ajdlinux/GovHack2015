# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patent', '0003_patentannotation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patentannotation',
            name='body',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='patentannotation',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='patentannotation',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='patentannotation',
            name='link_other',
            field=models.CharField(blank=True, null=True, max_length=100),
        ),
    ]
