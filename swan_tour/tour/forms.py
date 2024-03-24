from django import forms
from .models import Tour, TourReview, TourBooking, TourBookingName, TourImage
from django.forms import inlineformset_factory

class TourForm(forms.ModelForm):
    class Meta:
        model  = Tour
        fields = ['name', 'tour_type', 'group_size', 'city', 'place', 'map_link', 'rating', 'overview', 'no_of_day', 'itineraries', 'hotels', 'buses', 'start_date', 'end_date', 'total_price']
        # fields = '__all__'


class TourImageForm(forms.Form):

    class Meta:
        model = TourImage
        fields = ['tour', 'image']


class RepeatTourForm(forms.ModelForm):
    class Meta:
        model  = Tour
        fields = ['name', 'tour_type', 'city', 'place', 'rating', 'map_link', 'overview', 'no_of_day', 'itineraries', 'hotels', 'total_price']

# class TourBookingNameForm(forms.ModelForm):
#     class Meta:
#         model = TourBookingName
#         fields = ['first_name', 'last_name']

class TourBookingForm(forms.ModelForm):
    class Meta:
        model = TourBooking
        fields = ['user', 'tour', 'email', 'phone_number', 'first_name', 'last_name', 'start_date', 'end_date', 'no_of_people_booking', 'total_price']
        widgets = {
            
        }

class TourBookingNameForm(forms.ModelForm):
    class Meta:
        model = TourBookingName
        fields = ['first_name', 'last_name']
        # add custom widget class
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control bg_input'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control bg_input'}),
            
        }


TourBookingNameFormSet = inlineformset_factory




class TourReviewForm(forms.ModelForm):
    class Meta:
        model = TourReview
        fields = ['user', 'tour', 'rate', 'comment']

