#for testing only, will be removed later(sumit)

from django.http import JsonResponse
from .services import QuizGenerator


def test_subject_content(request, subject_id):

    content = QuizGenerator.get_subject_content(subject_id)

    return JsonResponse({
        "content": content
    })