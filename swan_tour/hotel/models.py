from django.db import models
from app.models import BaseModel
from core.models import City, Place, State
from django.contrib.auth.models import User
from django.core.exceptions import  ValidationError
from datetime import datetime
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator
import uuid
from autoslug import AutoSlugField
# Create your models here.
class Hotel(BaseModel):
    hotelname = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    map_link = models.URLField(max_length=500)
    total_room = models.IntegerField()
    price = models.IntegerField()
    rating =models.IntegerField(null=True, default=0)
    facility = models.CharField(max_length=100)
    # facilitys = models.ManyToManyField('Hotel_Facilitys', null=True, blank=True)
    overview = models.TextField(max_length=1000, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    hotel_image = models.ImageField(upload_to='image/hotel/')
    room_image = models.ImageField(upload_to='image/hotel/')
    image_3 = models.ImageField(upload_to='image/hotel/')
    image_4 = models.ImageField(upload_to='image/hotel/')
    image_5 = models.ImageField(upload_to='image/hotel/')
    hotel_slug = AutoSlugField(populate_from='hotelname', unique=True, null=True, default=None)
    

    # hotel rating auto updated
    @classmethod
    def update_rating(cls, hotel_id):
        hotel = cls.objects.get(id=hotel_id)
        reviews = Hotel_Review.objects.filter(hotel_id=hotel_id)
        average_rating = reviews.aggregate(models.Avg('rate'))['rate__avg']
        if average_rating is None:
            average_rating = 0
        hotel.rating = round(average_rating, 2)
        hotel.save()

    # Calculate available rooms based on booked rooms between 2 dates from start date to end date
    def get_available_rooms(self, date):
        booking_on_date = HotelBooking.objects.filter(hotel=self, valid_date_from__lte=date, valid_date_till__gte=date)

        total_booked_room = sum(booking.no_room_booking for booking in booking_on_date)
        return self.total_room - total_booked_room # now this thing get execute in hotel booking model at save function
    
    # return hotelname at django admin 
    def __str__(self) -> str:
        return str(self.hotelname)
    class Meta:
        ordering = ('created_at',)

#add after sometime
class Hotel_Review(BaseModel):
    
    def validate_max_value(value):
        if value > 5:
            raise ValidationError('Value must be equal to or below 5.0.')

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    rate = models.IntegerField(validators=[validate_max_value])
    comment = models.CharField(max_length=100)

    # update hotel rating
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.hotel.update_rating(self.hotel_id)
        
    def __str__(self) -> str:
        return str(self.hotel.hotelname)

    class Meta:
        ordering = ('created_at',)

class HotelBooking(BaseModel):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    valid_date_from = models.DateField(default=None)
    valid_date_till = models.DateField(default = None)
    no_room_booking = models.IntegerField()
    total_price = models.IntegerField()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.hotel.save()  # Update the hotel's available rooms after booking

    def clean(self):

        if self.no_room_booking > self.hotel.get_available_rooms(self.valid_date_from):
            raise ValidationError({'no_room_booking': 'Number of rooms booked cannot exceed available rooms'})
    
    def __str__(self) -> str:
        return str(self.hotel.hotelname)

    class Meta:
        ordering = ('created_at',)


class HotelImage(BaseModel):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='image/hotel/')


    def __str__(self) -> str:
        return str(self.hotel.hotelname)

    class Meta:
        ordering = ('created_at',)


class HotelFacilitys(BaseModel):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='image/hotel/')


    def __str__(self) -> str:
        return str(self.hotel.hotelname)

    class Meta:
        ordering = ('created_at',)