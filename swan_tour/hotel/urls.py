from django.urls import path, include
from .views import HotelView, HotelUserView
from app.views import ErrorView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # admin side hotel url
    path('new_hotel', HotelView.HotelCreateView.as_view(), name="new_hotel"),
    path('db_hotel_list', HotelView.HotelListView.as_view(), name="db_hotel_list"),
    path('hotel_delete/<int:pk>/', HotelView.HotelDeleteView.as_view(), name='hotel_delete'),
    path('hotel_update/<int:pk>', HotelView.HotelUpdateView.as_view(), name="hotel_update"),
    path('hotel_booking_list/', HotelView.HotleBookingListView.as_view(), name="hotel_booking_list"),

    # user side hotel view
    path('hotel_list/', HotelUserView.HotelListView.as_view(), name="hotel_list"),
    path('hotel_view', HotelUserView.UserHotelView.as_view(), name="hotel_view"),
    
    path('<str:undefined_route>/', ErrorView.as_view(), name='error'),
] + static(settings.MEDIA_ROOT, document_root=settings.MEDIA_ROOT)