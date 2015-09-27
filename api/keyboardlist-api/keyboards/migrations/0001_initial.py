# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Keyboard',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('model', models.CharField(max_length=255)),
                ('switch_type', models.CharField(choices=[('alps', 'ALPS'), ('buckling_spring', 'Buckling Spring'), ('cherry', 'Cherry MX'), ('kalih', 'Kalih'), ('other', 'Other')], max_length=255)),
                ('size', models.CharField(choices=[('tkl', 'Tenkeyless'), ('full', 'Full Size'), ('other', 'Other')], max_length=255)),
                ('led', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('url', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='keyboard',
            name='manufacturer',
            field=models.ForeignKey(to='keyboards.Manufacturer', null=True, blank=True, on_delete=django.db.models.deletion.SET_NULL),
        ),
    ]
