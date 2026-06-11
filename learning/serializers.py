from rest_framework import serializers
from .models import Subject, Unit, Topic

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Subject
        fields='__all__'

class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model=Unit
        fields='__all__'

class TopicSerializer(serializers.ModelSerializer):
    unit_slug = serializers.SlugRelatedField(source='unit', read_only=True, slug_field='slug')

    class Meta:
        model=Topic
        fields=('id', 'unit', 'unit_slug', 'title', 'slug', 'markdown_content', 'order', 'created_at')
