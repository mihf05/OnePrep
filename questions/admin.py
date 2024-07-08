from django.contrib import admin
from djangoql.admin import DjangoQLSearchMixin
from import_export import resources

from .models import Question, AnswerChoice, Answer
from .models import UserQuestionAnswer
from .models import UserQuestionStatus, UserQuestionAnswerStatus


@admin.register(Question)
class QuestionAdmin(DjangoQLSearchMixin, admin.ModelAdmin):
    list_display = [
        'id',
        'source_id',
        # 'source_id_2',
        # 'source_id_3',
        'module',
        'program',
        # 'stimulus',
        # 'stem',
        'difficulty',
        'answer_type',
        # 'explanation',
        # 'raw',
        'source',
        'source_order',
        'created',
        'modified',
        'added_by',
    ]
    list_filter = [
        'program',
        'source',
        # 'created_at',
        # 'updated_at',
        'module',
        'difficulty',
        'answer_type',
        'added_by',
    ]
    search_fields = [
        'source',
        'source_id',
        'source_id_2',
        'source_id_3',
        'stimulus',
        'stem',
        'explanation',
        # 'added_by__username',
        'added_by__email',
    ]

    raw_id_field = ['added_by']
    # date_hierarchy = 'created_at'


@admin.register(AnswerChoice)
class AnswerChoiceAdmin(DjangoQLSearchMixin, admin.ModelAdmin):
    list_display = [
        'id',
        'question',
        # 'text',
        # 'explanation',
        'is_correct',
        'letter',
        'order',
    ]
    list_filter = [
        # 'question',
        'is_correct',
        'letter',
    ]
    search_fields = [
        'question__source_id',
        'question__source_id_2',
        'question__source_id_3',
        'question__source',
        'question__module',
        'question__stimulus',
        'question__stem',
        'question__difficulty',
        'question__explanation',
        # 'question__added_by__username',
        'question__added_by__email',
        'question__tags__name',
        'text',
        'explanation',
    ]

    raw_id_field = ['question']


@admin.register(Answer)
class AnswerAdmin(DjangoQLSearchMixin, admin.ModelAdmin):
    list_display = [
        'id',
        'question',
        'value',
        # 'explanation',
        'order'
    ]
    list_filter = []
    raw_id_fields = ['question']


@admin.register(UserQuestionAnswer)
class UserQuestionAnswerAdmin(DjangoQLSearchMixin, admin.ModelAdmin):
    list_display = [
        'id',
        'user',
        'question',
        'exam',
        'answer_choice',
        'answer',
        'is_correct',
        'time_given',
        'started_at',
        'answered_at',
    ]
    list_filter = [
        'is_correct',
    ]
    search_fields = [
        'user__username',
        'user__email',
        'question__source_id',
        'question__source_id_2',
        'question__source_id_3',
        'question__source',
        'question__module',
        'question__stimulus',
        'question__stem',
        'question__difficulty',
        'question__explanation',
        'question__added_by__username',
        'question__added_by__email',
        'question__tags__name',
        'answer_choice__text',
        'answer',
    ]
    raw_id_fields = ['user', 'question', 'exam', 'answer_choice']
