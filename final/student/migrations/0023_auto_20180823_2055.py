# Generated by Django 2.0.6 on 2018-08-23 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0022_auto_20180823_1816'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student_form2',
            old_name='Twelfth_result',
            new_name='Status_of_twefth_result',
        ),
        migrations.RenameField(
            model_name='student_form2',
            old_name='tenth_marks',
            new_name='marks_in_tenth',
        ),
        migrations.RenameField(
            model_name='student_form3',
            old_name='Twelfth_marks',
            new_name='marks_in_twelfth',
        ),
        migrations.RenameField(
            model_name='student_form4',
            old_name='signature_photo',
            new_name='candidate_signature',
        ),
        migrations.RenameField(
            model_name='student_form4',
            old_name='thumb_photo',
            new_name='thumb_impression',
        ),
    ]