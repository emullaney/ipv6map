# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import csv
import os

from django.db import models, migrations

def no_op(apps, schema_editor):
    # Do nothing on reversal
    pass

def create_city_data(apps, schema_editor):
    # Load the ipv6Address model and open CSV file
    # to load in all ipv6 address data

    ipv6Address = apps.get_model('heatmap', 'ipv6Address')

    base = os.path.dirname(os.path.abspath(__file__))
    base = os.path.dirname(base) + '/data'
    with open(os.path.join(base, "GeoLite2-City-Blocks-IPv6.csv")) as csvfile:
        next(csvfile)  # Skip the first line, header line
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            ipv6Address.objects.create(
                network = row[0],
                geoname_id = row[1],
                postal_code = row[6],
                latitude = row[7],
                longitude = row[8])


class Migration(migrations.Migration):

    dependencies = [
        ('heatmap', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_city_data, no_op),
    ]