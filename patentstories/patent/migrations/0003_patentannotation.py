# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('patent', '0002_auto_20150704_0712'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatentAnnotation',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('annotation_type', models.IntegerField(default=0)),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('link', models.URLField()),
                ('link_other', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('creator', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('patent_application', models.ForeignKey(to='patent.PatentApplication')),
            ],
        ),
    ]
