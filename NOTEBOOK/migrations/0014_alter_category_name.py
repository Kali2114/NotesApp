# Generated by Django 5.0.2 on 2024-02-29 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NOTEBOOK', '0013_alter_category_name_remove_note_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('Work', 'Work'), ('Personal', 'Personal'), ('Project', 'Project'), ('Hobby', 'Hobby'), ('Science', 'Science'), ('Health and Sport', 'Health and Sport'), ('Finances', 'Finances'), ('Other', 'Other')], max_length=100, unique=True),
        ),
    ]
