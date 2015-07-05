# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('patent', '0008_auto_20150705_0108'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExternalCachedData',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('adapter_code', models.CharField(max_length=16)),
                ('data', jsonfield.fields.JSONField()),
                ('patent_application', models.ForeignKey(to='patent.PatentApplication')),
            ],
        ),
    ]
