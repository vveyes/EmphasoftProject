from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import RoomList, RoomDetail, BookRoomList, SignupView, UserDetail

urlpatterns = [
    path('', lambda request: redirect('rooms_list'), name='home'),
    path('registration/', SignupView.as_view(), name='register'),
    path('profile/', UserDetail.as_view(), name='user_profile'),
    path('login/', obtain_auth_token, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),  
    path('rooms', RoomList.as_view(), name='rooms_list'),
    path('room/<int:room_id>', RoomDetail.as_view(), name='room_detail'),
    path('books', BookRoomList.as_view(), name='book_list'),
]
