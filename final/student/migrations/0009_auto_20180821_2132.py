# Generated by Django 2.0.6 on 2018-08-21 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0008_auto_20180821_2118'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student_form4',
            old_name='f1',
            new_name='user',
        ),
    ]