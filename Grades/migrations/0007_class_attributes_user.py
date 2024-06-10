# Generated by Django 4.1.5 on 2024-05-26 01:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Grades', '0006_rename_classsection_class_attributes_classrequirement'),
    ]

    operations = [
        migrations.AddField(
            model_name='class_attributes',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
