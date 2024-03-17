from django import forms
# from django.forms import inlineformset_factory
from .models import Hotel, HotelBooking, HotelFacilitys, HotelImage

class HotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = ['hotelname', 'address', 'map_link', 'total_room', 'price', 'rating', 'facility', 'city', 'hotel_image', 'room_image', 'image_3', 'image_4', 'image_5']

class HotelBookingForm(forms.ModelForm):
    class Meta:
        model = HotelBooking
        fields = ['user', 'hotel', 'first_name', 'last_name', 'valid_date_from', 'valid_date_till', 'no_room_booking', 'total_price']


class HotelImageForm(forms.ModelForm):
    class Meta:
        model = HotelImage
        fields = ['hotel', 'image']


class HotelFacilitysForm(forms.ModelForm):
    class Meta:
        model = HotelFacilitys
        fields = ['name', 'image']