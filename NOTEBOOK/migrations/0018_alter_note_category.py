# Generated by Django 5.0.2 on 2024-02-29 20:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NOTEBOOK', '0017_alter_category_name_alter_note_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='category',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category', to='NOTEBOOK.category'),
        ),
    ]
