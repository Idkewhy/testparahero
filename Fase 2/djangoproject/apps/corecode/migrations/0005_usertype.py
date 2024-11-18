# Generated by Django 4.2.7 on 2024-11-01 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("corecode", "0004_auto_20201124_0614"),
    ]

    operations = [
        migrations.CreateModel(
            name="UserType",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200, unique=True)),
            ],
            options={
                "verbose_name": "Tipo de Usuario",
                "verbose_name_plural": "Tipos de Usuario",
                "ordering": ["name"],
            },
        ),
    ]
