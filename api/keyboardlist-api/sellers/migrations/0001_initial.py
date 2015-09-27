# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('keyboards', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='KeyboardInventory',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('price', models.IntegerField()),
                ('url', models.URLField()),
                ('switch_type', models.CharField(max_length=255)),
                ('stock', models.CharField(max_length=50, choices=[('out_of_stock', 'Out of Stock'), ('unknown', 'Unknown'), ('available', 'Available')])),
                ('keyboard', models.ForeignKey(to='keyboards.Keyboard')),
            ],
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('domain', models.URLField()),
            ],
        ),
        migrations.AddField(
            model_name='keyboardinventory',
            name='seller',
            field=models.ForeignKey(to='sellers.Seller'),
        ),
    ]
