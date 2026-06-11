from django.contrib import admin
from .models import Question


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "subject",
        "topic",
        "level"
    )

    list_filter = (
        "subject",
        "level"
    )

    search_fields = (
        "question_text",
    )