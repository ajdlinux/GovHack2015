# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patent', '0007_featuredstory'),
    ]

    operations = [
        migrations.AddField(
            model_name='patentannotation',
            name='image',
            field=models.ImageField(null=True, upload_to='annotation/', blank=True),
        ),
        migrations.AddField(
            model_name='patentannotation',
            name='image_alt',
            field=models.CharField(null=True, max_length=100, blank=True),
        ),
    ]
