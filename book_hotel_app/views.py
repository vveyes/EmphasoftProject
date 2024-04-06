
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse_lazy

from rest_framework import generics
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


from .models import BookRoom, Room, User
from .serializers import BookRoomSerializer, RoomSerializer, UserSerializer
from .permissions import OwnerOrReadOnly
from .filters import RoomFilter, BookRoomFilter

#Список всех комнат
class RoomList(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = RoomFilter
    ordering_fields = ['cost', 'room_capacity']

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset


# Детальное описание комнаты, согласно ТЗ
class RoomDetail(generics.RetrieveAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    lookup_field = 'room_id'


# Список всех забранированных комнат
class BookRoomList(generics.ListAPIView):
    queryset = BookRoom.objects.all()
    serializer_class = BookRoomSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = BookRoomFilter


# Детали о пользователе

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (OwnerOrReadOnly,)
    def get_object(self):
        return self.request.user

# Регистрация пользователя
class SignupView(generics.CreateAPIView):
    serializer_class = UserSerializer
    success_url = reverse_lazy('login')