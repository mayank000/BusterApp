# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('busterapp', '0003_auto_20181203_1825'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskChild',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, null=True, blank=True)),
                ('added_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_on', models.DateTimeField(auto_now=True, null=True)),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='busterapp.Task', null=True)),
            ],
            options={
                'db_table': 'TaskChild',
                'verbose_name': 'TaskChild',
                'verbose_name_plural': 'TaskChilds',
            },
        ),
    ]
