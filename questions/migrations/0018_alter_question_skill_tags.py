# Generated by Django 5.0.6 on 2024-08-10 12:07

import taggit.managers
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        ('questions', '0017_alter_question_source_raw_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='skill_tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='core.SkillTagged', to='core.SkillTag', verbose_name='Tags'),
        ),
    ]
