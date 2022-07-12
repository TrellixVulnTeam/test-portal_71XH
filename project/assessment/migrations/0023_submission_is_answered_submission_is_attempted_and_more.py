# Generated by Django 4.0.6 on 2022-07-10 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0022_rename_is_subjective_question_is_range_present'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='is_answered',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='submission',
            name='is_attempted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='submission',
            name='is_reviewed',
            field=models.BooleanField(default=False),
        ),
    ]
