from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import RoomList, RoomDetail, BookRoomList, SignupView, UserProfileView

urlpatterns = [
    path('registration/', SignupView.as_view(), name='register'),
    path('profile/', UserProfileView.as_view(), name='user_profile'),
    path('login/', LoginView.as_view(template_name='book_hotel_app/login.html', success_url='rooms_list'),
         name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('rooms', RoomList.as_view(), name='rooms_list'),
    path('room/<int:room_id>', RoomDetail.as_view(), name='room_detail'),
    path('books', BookRoomList.as_view(), name='book_list'),
]
