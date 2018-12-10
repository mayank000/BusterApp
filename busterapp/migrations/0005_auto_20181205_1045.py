# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('busterapp', '0004_taskchild'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taskchild',
            name='added_by',
        ),
        migrations.AddField(
            model_name='task',
            name='parent',
            field=models.ForeignKey(blank=True, to='busterapp.Task', null=True),
        ),
        migrations.DeleteModel(
            name='TaskChild',
        ),
    ]
