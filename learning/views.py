from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Subject, Unit, Topic
from .serializers import SubjectSerializer, UnitSerializer, TopicSerializer

class SubjectListView(APIView):
    def get(self, request):
        serializer=SubjectSerializer(Subject.objects.all().order_by('name'), many=True)
        return Response(serializer.data)

class SubjectUnitsView(APIView):
    def get(self, request, slug):
        subject=get_object_or_404(Subject, slug=slug)
        serializer=UnitSerializer(subject.units.all().order_by('order', 'id'), many=True)
        return Response(serializer.data)

class UnitTopicsView(APIView):
    def get(self, request, slug):
        unit=get_object_or_404(Unit, slug=slug)
        serializer=TopicSerializer(unit.topics.all().order_by('order', 'id'), many=True)
        return Response(serializer.data)

class TopicDetailView(APIView):
    def get(self, request, slug):
        topic=get_object_or_404(Topic, slug=slug)
        serializer=TopicSerializer(topic)
        return Response(serializer.data)
