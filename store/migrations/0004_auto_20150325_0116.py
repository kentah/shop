# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20150325_0114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='tags',
            field=models.ManyToManyField(to='store.Tag'),
            preserve_default=True,
        ),
    ]
