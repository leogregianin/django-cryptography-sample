from rest_framework import serializers

from field.models import Field, FieldDetails


class FieldDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FieldDetails
        fields = '__all__'


class FieldSerializer(serializers.ModelSerializer):

    details = FieldDetailsSerializer(many=True)

    class Meta:
        model = Field
        fields = [
            'id',
            'name',
            'sensitive_data',
            'details'
        ]
