from rest_framework import serializers

from requests.models import Request


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request

    def create(self, validated_data):
        print validated_data
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Request.objects.create(**validated_data)