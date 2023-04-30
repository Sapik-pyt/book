from djoser.serializers import UserCreateSerializer, UserSerializer
from read.models import Book, User
from rest_framework import serializers


class UserCustomRegSerializer(UserCreateSerializer):
    """
    Сериализатор для регистрации пользователя.
    """
    class Meta:
        model = User
        fields = (
            "id", "username", "password", "first_name", "last_name", "birthday"
        )
        extra_kwargs = {
            'password': {'write_only': True},
            'birthday': {'required': True}
        }

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data["username"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            birthday=validated_data["birthday"],
        )
        user.set_password(validated_data["password"])
        user.save()
        return user


class CustomUserSerializer(UserSerializer):
    """
    Сериалайзер модели пользователя.
    """
    class Meta:
        model = User
        fields = ("id", "username", "first_name", "last_name",)


class BookSerializer(serializers.ModelSerializer):
    """
    Сериалайзер книг.
    """
    author = CustomUserSerializer(read_only=True)

    class Meta:
        model = Book
        fields = "__all__"
        extra_kwargs = {
            "text": {"required": True},
            "pub_date": {"required": True}
        }

    def create(self, validated_data):
        author = self.context.get("request").user
        book = Book.objects.create(author=author, **validated_data)
        return book

    def update(self, instance, validated_data):
        Book.objects.filter(title=instance).delete()
        return super().update(instance, validated_data)
