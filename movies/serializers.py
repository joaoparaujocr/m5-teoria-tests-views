from rest_framework import serializers

class MovieSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.CharField()