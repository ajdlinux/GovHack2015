# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('patent', '0005_auto_20150704_1038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patentannotation',
            name='creator',
            field=models.ForeignKey(blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
