# Generated by Django 4.2.7 on 2024-11-03 01:12

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("content", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="content",
            name="description",
            field=ckeditor.fields.RichTextField(),
        ),
    ]
