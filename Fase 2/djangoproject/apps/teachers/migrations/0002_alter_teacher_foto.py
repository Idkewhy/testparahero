# Generated by Django 4.2.7 on 2024-11-01 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("teachers", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="teacher",
            name="foto",
            field=models.ImageField(blank=True, upload_to="teachers/fotos/"),
        ),
    ]
