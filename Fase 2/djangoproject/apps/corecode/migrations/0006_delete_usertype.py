# Generated by Django 4.2.7 on 2024-11-01 02:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("students", "0006_remove_student_tipo_usuario"),
        ("corecode", "0005_usertype"),
    ]

    operations = [
        migrations.DeleteModel(
            name="UserType",
        ),
    ]
