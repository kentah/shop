# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_joinform'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Album',
        ),
        migrations.RenameField(
            model_name='joinform',
            old_name='first',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='joinform',
            old_name='last',
            new_name='last_name',
        ),
        migrations.RenameField(
            model_name='joinform',
            old_name='pass_word',
            new_name='password',
        ),
        migrations.RenameField(
            model_name='joinform',
            old_name='user_name',
            new_name='username',
        ),
        migrations.AlterField(
            model_name='joinform',
            name='email',
            field=models.EmailField(null=True, blank=True, max_length=60),
            preserve_default=True,
        ),
    ]
