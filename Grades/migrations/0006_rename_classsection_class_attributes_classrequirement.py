# Generated by Django 4.1.5 on 2024-05-25 19:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Grades', '0005_class_attributes_remove_class_grade_classname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='class_attributes',
            old_name='classSection',
            new_name='classRequirement',
        ),
    ]
