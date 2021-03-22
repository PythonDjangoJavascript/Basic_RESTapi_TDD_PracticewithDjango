from rest_framework import serializers


class HelloApiSerializer(serializers.Serializer):
    """Serializes a name and occupation field for our test APIView"""

    name = serializers.CharField(max_length=20)
    is_employed = serializers.BooleanField(default=True)
    occupation = serializers.CharField(max_length=25)
