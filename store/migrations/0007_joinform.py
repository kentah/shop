# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20150329_0103'),
    ]

    operations = [
        migrations.CreateModel(
            name='JoinForm',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('first', models.CharField(blank=True, null=True, max_length=60)),
                ('last', models.CharField(blank=True, null=True, max_length=60)),
                ('user_name', models.CharField(blank=True, null=True, max_length=20)),
                ('pass_word', models.CharField(blank=True, null=True, max_length=10)),
                ('email', models.CharField(blank=True, null=True, max_length=60)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
