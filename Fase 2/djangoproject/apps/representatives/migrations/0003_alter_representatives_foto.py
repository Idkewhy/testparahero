# Generated by Django 4.2.7 on 2024-11-01 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("representatives", "0002_alter_representatives_foto"),
    ]

    operations = [
        migrations.AlterField(
            model_name="representatives",
            name="foto",
            field=models.ImageField(blank=True, upload_to="students/fotos/"),
        ),
    ]
