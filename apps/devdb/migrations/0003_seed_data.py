# Generated by Django 3.1.7 on 2021-02-21 05:26

import json
from pathlib import Path

from django.db import migrations

HERE = Path(__file__).parent


def insert_data(apps, schema_editor):
    data = json.load((HERE / "seed_data.json").open("rb"))
    Developer = apps.get_model("devdb", "Developer")
    Developer.objects.bulk_create(
        Developer(**d["fields"]) for d in data if d["model"] == "devdb.developer"
    )


class Migration(migrations.Migration):

    dependencies = [
        ("devdb", "0002_add_firstname_lastname"),
    ]

    operations = [migrations.RunPython(insert_data)]