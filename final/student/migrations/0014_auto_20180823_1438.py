# Generated by Django 2.0.6 on 2018-08-23 09:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('student', '0013_auto_20180823_1422'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student_form1',
            name='user',
        ),
        migrations.AddField(
            model_name='student_form1',
            name='f1',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
