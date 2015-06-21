# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_image_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='description',
            field=models.TextField(default='\n    Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. \n    Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor \n    in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, \n    sunt in culpa qui officia deserunt mollit anim id est laborum.\n    '),
            preserve_default=True,
        ),
    ]
