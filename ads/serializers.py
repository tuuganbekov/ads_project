from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model

from .models import Category, Ad, AdImage

User = get_user_model()

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email",]


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class AdImageSerializer(ModelSerializer):
    class Meta:
        model = AdImage
        fields = "__all__"


class AdSerializer(ModelSerializer):
    author = UserSerializer(read_only=True)
    images = AdImageSerializer(many=True, read_only=True)

    class Meta:
        model = Ad
        fields = [
            "id", "title", "body", "active", "category", "author", "images",
        ]

    def create(self, validated_data):
        request = self.context.get("request")
        files = request.FILES.getlist("images")
        validated_data["author"] = request.user
        ad = Ad.objects.create(**validated_data)
        for image in files:    
            AdImage.objects.create(
                ad=ad,
                image=image
            )
        return ad
