import django_filters
from .models import Room, BookRoom

class RoomFilter(django_filters.FilterSet):
    room_capacity = django_filters.NumberFilter(field_name='room_capacity', lookup_expr='exact')
    cost = django_filters.NumberFilter(field_name='cost', lookup_expr='exact')
    class Meta:
        model = Room
        fields = {
            'name_room_type': ['exact'],
            'cost': ['gte', 'lte'],
        }

class BookRoomFilter(django_filters.FilterSet):
    class Meta:
        model = BookRoom
        fields = {
            'user__username': ['exact'],
            'room__name_room_type': ['exact'],
            'check_in_date': ['gte', 'lte'],
            'check_out_date': ['gte', 'lte'],
        }