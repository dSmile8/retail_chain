# Generated by Django 4.2 on 2024-09-17 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("retail", "0008_alter_contact_chain_line"),
    ]

    operations = [
        migrations.AddField(
            model_name="chain",
            name="is_factory",
            field=models.BooleanField(default=False, verbose_name="Завод"),
        ),
    ]
