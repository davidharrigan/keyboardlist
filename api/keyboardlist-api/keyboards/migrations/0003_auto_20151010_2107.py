# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('keyboards', '0002_auto_20150928_0304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keyboard',
            name='switch_type',
            field=models.CharField(max_length=255, choices=[('alps', 'ALPS'), ('buckling_spring', 'Buckling Spring'), ('cherry', 'Cherry MX'), ('kailh', 'Kailh'), ('matias', 'Matias'), ('other', 'Other')]),
        ),
    ]
