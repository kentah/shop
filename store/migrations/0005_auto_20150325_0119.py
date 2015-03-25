# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20150325_0116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='tags',
            field=models.ManyToManyField(to='store.Tag', blank=True),
            preserve_default=True,
        ),
    ]
