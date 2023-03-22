from rest_framework import serializers

from .models import ExampleModel


class ExampleModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExampleModel
        fields = "__all__"

    def validate_name(self, value):
        # Custom validation logic here
        return value
