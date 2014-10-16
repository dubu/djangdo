# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mandu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('seq', models.IntegerField()),
                ('name', models.CharField(max_length=30)),
                ('count', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
