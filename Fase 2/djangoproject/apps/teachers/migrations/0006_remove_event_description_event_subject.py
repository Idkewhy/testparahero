# Generated by Django 4.2.7 on 2024-11-05 03:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("corecode", "0008_alter_subject_name"),
        ("teachers", "0005_event_alter_annotation_annotation_type"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="event",
            name="description",
        ),
        migrations.AddField(
            model_name="event",
            name="subject",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="events",
                to="corecode.subject",
            ),
        ),
    ]
