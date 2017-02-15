# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-14 17:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturas', '0004_factura_cobrada'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factura',
            name='total',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=6),
        ),
    ]