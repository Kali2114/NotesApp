# Generated by Django 5.0.2 on 2024-03-02 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NOTEBOOK', '0018_alter_note_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='priority',
            field=models.CharField(choices=[('High', 'High'), ('Normal', 'Normal'), ('Low', 'Low'), ('None', 'None')], default='None', max_length=10),
        ),
    ]