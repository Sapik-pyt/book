from djoser.views import UserViewSet
from read.models import Book, User
from read.permissions import IsAuthorOrReadOnly
from read.serializers import BookSerializer, CustomUserSerializer
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class CustomUserViewSet(UserViewSet):
    """
    Viewset для работы с пользователям.
    """
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer


class ReadView(viewsets.ModelViewSet):
    """
    APIView для создания, просмотра, удаления и редактирования книги.
    """
    queryset = Book.objects.all()

    serializer_class = BookSerializer

    @action(
        detail=True, methods=['post'], permission_classes=(IsAuthenticated,)
    )
    def create_book(self, request, pk=None):
        data = ({"author": request.user.id, "book_id": pk})
        serializer = BookSerializer(data=data, context={"request": request})
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True, permission_classes=(IsAuthorOrReadOnly,))
    @create_book.mapping.delete
    def delete_book(self, request, pk):
        book = get_object_or_404(Book, id=pk, author=request.user)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
