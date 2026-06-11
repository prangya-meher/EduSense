from django.urls import path
from .views import test_subject_content

urlpatterns = [
    path(
        "test-subject-content/<int:subject_id>/",
        test_subject_content
    ),
]