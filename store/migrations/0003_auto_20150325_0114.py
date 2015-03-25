# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20150325_0113'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='tag',
        ),
        migrations.AddField(
            model_name='image',
            name='tags',
            field=models.ManyToManyField(blank=True, to='store.Tag'),
            preserve_default=True,
        ),
    ]
