# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Units',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('source', models.TextField()),
                ('source_plural', models.TextField()),
                ('context', models.TextField()),
                ('target', models.TextField()),
                ('project', models.ForeignKey(to='projects.Projects')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
