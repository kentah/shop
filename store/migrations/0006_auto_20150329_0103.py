# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20150325_0119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='store/static/store_images/'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='image',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
            preserve_default=True,
        ),
    ]
