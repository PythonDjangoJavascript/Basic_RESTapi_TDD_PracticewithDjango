from rest_framework import fields, serializers
from core.models import User
from core.models import ProfileFeedItem


class HelloApiSerializer(serializers.Serializer):
    """Serializes a name and occupation field for our test APIView"""

    name = serializers.CharField(max_length=20)
    is_employed = serializers.BooleanField(default=True)
    occupation = serializers.CharField(max_length=25)


class UserProfileSerializser(serializers.ModelSerializer):
    """Serializes User profile model objects"""

    class Meta:
        """We use meta on model class to define models attribute"""

        model = User
        fields = ('email', 'name', 'password')

        extra_kwargs = {
            "password": {
                "write_only": True,
                "style": {"input_type": "password"},
                "min_length": 5
            }
        }

        def create(self, validated_data):
            """Overrinding create function to create encripted password"""

            user = User.objects.create_user(
                email=validated_data["email"],
                name=validated_data["name"],
                password=validated_data["password"]
            )

            return user

        # def create(self, validated_data):
        #     return User.objects.create_user(**validated_data)


class ProfileFeedSerializer(serializers.ModelSerializer):
    """Serializes users feed Item"""

    class Meta:
        model = ProfileFeedItem
        fields = (
            "user_profile",
            "status_text",
            "created_on"
        )

        extra_kwargs = {
            "user_profile":}
