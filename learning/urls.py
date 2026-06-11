from django.urls import path
from .views import SubjectListView, SubjectUnitsView, UnitTopicsView, TopicDetailView

urlpatterns=[
    path('subjects/', SubjectListView.as_view()),
    path('subjects/<slug:slug>/units/', SubjectUnitsView.as_view()),
    path('units/<slug:slug>/topics/', UnitTopicsView.as_view()),
    path('topic/<slug:slug>/', TopicDetailView.as_view()),
]
