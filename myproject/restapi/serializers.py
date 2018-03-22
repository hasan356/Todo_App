from rest_framework import serializers
from .objects import TodoObject
from .models import TodoModel

class TodoSerializer(serializers.Serializer):
    todo_id = serializers.CharField(required=False, read_only=True)
    title_id = serializers.IntegerField()
    title = serializers.CharField()
    description = serializers.CharField()
    created_at = serializers.DateTimeField(required=False, read_only=True)

    def update(self, instance, validated_data):
        instance.title_id = validated_data.get('title_id', instance.title)
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance

    def create(self, validated_data):
        return TodoModel.objects.create(**validated_data)