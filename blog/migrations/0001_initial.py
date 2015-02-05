# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('post_header', models.CharField(max_length=200)),
                ('post_date', models.DateTimeField(verbose_name='date published')),
                ('post_content', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
