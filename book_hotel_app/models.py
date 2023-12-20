from django.db import models
from django.contrib.auth.models import User


class Room(models.Model):
    ROOM_TYPES = [
        ('Standart Room', 'Standart Room'),
        ('Suite Room', 'Suite Room'),
        ('Luxury Room', 'Luxury Room'),
        ('Middle Suite Room', 'Middle Suite Room'),
        ('Studio Room', 'Studio Room'),
    ]
    room_id = models.IntegerField(unique=True)
    name_room_type = models.CharField(max_length=50, choices=ROOM_TYPES)
    cost = models.IntegerField()
    room_capacity = models.IntegerField()

    class Meta:
        db_table = 'room_table'

    def is_available(self, check_in_date, check_out_date):
        bookings = BookRoom.objects.filter(room=self,
                                           check_in_date__lt=check_out_date,
                                           check_out_date__gt=check_in_date)
        return not bookings.exists()


class BookRoom(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()

    class Meta:
        db_table = 'book_table'


