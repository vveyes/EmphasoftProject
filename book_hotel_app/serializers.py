from rest_framework import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from book_hotel_app.models import Room, BookRoom, User


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['room_id', 'name_room_type', 'cost', 'room_capacity']


class BookRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookRoom
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

'''class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = {'username', 'email', 'first_name', 'last_name', 'password'}

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user'''