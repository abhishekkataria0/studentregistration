# Generated by Django 2.0.6 on 2018-09-11 14:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0026_student_form1_ten_marksheet'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student_form1',
            name='ten_marksheet',
        ),
        migrations.AddField(
            model_name='student_form4',
            name='ref_id',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
