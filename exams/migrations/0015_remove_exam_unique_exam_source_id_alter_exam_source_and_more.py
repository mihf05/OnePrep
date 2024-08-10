# Generated by Django 5.0.6 on 2024-08-10 11:43

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        ('exams', '0014_alter_exam_skill_tags_alter_exam_tags'),
        ('taggit', '0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='exam',
            name='unique_exam_source_id',
        ),
        migrations.AlterField(
            model_name='exam',
            name='source',
            field=models.CharField(blank=True, default='', max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='exam',
            name='source_id',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AddConstraint(
            model_name='exam',
            constraint=models.UniqueConstraint(condition=models.Q(models.Q(('source__isnull', False), models.Q(('source', ''), _negated=True), _connector='OR'), models.Q(('source_id__isnull', False), models.Q(('source_id', ''), _negated=True), _connector='OR')), fields=('source', 'source_id'), name='unique_exam_source_id'),
        ),
    ]
