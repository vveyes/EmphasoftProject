from django.contrib import messages
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import user_passes_test
from django.views import View
from django.views.generic import CreateView, DetailView
from rest_framework import generics
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import BookRoom, Room, User
from .serializers import BookRoomSerializer, RoomSerializer, UserSerializer
from .permissions import OwnerOrReadOnly
from .forms import RegisterForm, ReservationForm

#Список всех комнат

class RoomList(generics.ListAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'book_hotel_app/roomlist.html'
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    def get(self, request, *args, **kwargs):
        cost = request.query_params.get('cost', None)
        room_capacity = request.query_params.get('room_capacity', None)

        # Фильтрация по параметрам
        queryset = self.get_queryset()
        if cost:
            queryset = queryset.filter(cost=cost)
        if room_capacity:
            queryset = queryset.filter(room_capacity=room_capacity)

        # Сериализация и возврат ответа
        serializer = self.get_serializer(queryset, many=True)
        return Response({'rooms': serializer.data})


# Детальное описание комнаты, согласно ТЗ
class RoomDetail(View):
    template_name = 'book_hotel_app/room_detail.html'

    def get(self, request, room_id):
        room = get_object_or_404(Room, room_id=room_id)
        user_bookings = BookRoom.objects.filter(user=request.user, room=room) if request.user.is_authenticated else None
        all_bookings = BookRoom.objects.filter(room=room) if request.user.is_superuser else None
        book_form = ReservationForm()

        return render(request, self.template_name,
                      {'room': room, 'user_bookings': user_bookings, 'all_bookings': all_bookings,
                       'book_form': book_form})

    def post(self, request, room_id):
        room = get_object_or_404(Room, room_id=room_id)

        if 'check_in_date' in request.POST and 'check_out_date' in request.POST:
            booking_form = ReservationForm(request.POST)

            if booking_form.is_valid():
                booking = booking_form.save(commit=False)

                if room.is_available(booking.check_in_date, booking.check_out_date):
                    booking.user = request.user
                    booking.room = room
                    booking.save()
                    return redirect('room_detail', room_id=room.room_id)
                else:
                    messages.error(request, 'Комната уже забронирована на указанный период.')
        elif 'cancel_booking' in request.POST:
            booking_id = request.POST.get('cancel_booking')

            if booking_id:
                booking = get_object_or_404(BookRoom, id=booking_id)

                if not request.user.is_superuser and request.user != booking.user:
                    return HttpResponseForbidden('У вас нет прав на отмену бронирования')

                booking.delete()
                return redirect('room_detail', room_id=room.room_id)


# Список всех забранированных комнат
class BookRoomList(generics.ListAPIView):
    queryset = BookRoom.objects.all()
    serializer_class = BookRoomSerializer


# Детали о пользователе

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (OwnerOrReadOnly,)
    template_name = 'book_hotel_app/user_profile.html'


class SignupView(CreateView):
    template_name = 'book_hotel_app/registration.html'
    form_class = RegisterForm
    success_url = reverse_lazy('login')


class UserProfileView(LoginRequiredMixin, DetailView):
    template_name = 'book_hotel_app/user_profile.html'
    context_object_name = 'user'
    model = User

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['bookings'] = BookRoom.objects.filter(user=user)
        context['rooms'] = Room.objects.filter(bookroom__user=user)
        return context
