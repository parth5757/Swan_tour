from django.db import models
from app.models import BaseModel
from core.models import City, Place
from bus.models import Bus
from hotel.models import Hotel  
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from autoslug import AutoSlugField
import datetime
from django.utils import timezone
# from django.contrib.auth.models import User
# from django.contrib.postgres.fields import JSONField
# from django.urls import reverse_lazy

class TourType(BaseModel):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='image/tour_type/', blank=True, null=True)

    # return Tour typr name at django admin 
    def __str__(self) -> str:
        return str(self.name)
    
    class Meta:
        ordering = ('created_at',)

class Tour(BaseModel):
    name = models.CharField(max_length=200)
    tour_type = models.ForeignKey(TourType, on_delete=models.CASCADE, related_name='type')
    group_size = models.IntegerField()
    city = models.ManyToManyField(City, related_name='citys')
    place = models.ManyToManyField(Place, related_name='places')
    map_link = models.URLField(max_length=500)
    rating =models.IntegerField(null=True, default=0)
    overview = models.TextField(max_length=2000)
    no_of_day = models.IntegerField(default=0)
    itineraries = models.JSONField(default=dict)
    included = models.JSONField(default=dict)
    hotels = models.ManyToManyField(Hotel, related_name='hotels')
    buses = models.ManyToManyField(Bus, related_name='buss')
    start_date = models.DateField(default=None)
    end_date = models.DateField(default = None)
    tour_image = models.ImageField(upload_to='image/tour/', null=True, blank=True)
    image_2 = models.ImageField(upload_to='image/tour/', null=True, blank=True)
    image_3 = models.ImageField(upload_to='image/tour/', null=True, blank=True)
    total_price = models.IntegerField()
    tour_slug = AutoSlugField(populate_from='name', unique=True, null=True, default=None)

    @classmethod
    def update_rating(cls, tour_id):
        hotel = cls.objects.get(id=tour_id)
        reviews = TourReview.objects.filter(tour_id=tour_id)
        average_rating = reviews.aggregate(models.Avg('rate'))['rate__avg']
        if average_rating is None:
            average_rating = 0
        hotel.rating = round(average_rating, 2)
        hotel.save()

    def get_available_group_size(self):
        group_size = self.group_size
        total_booked_tour = TourBooking.objects.filter(tour=self).aggregate(total_booked=models.Sum('no_of_people_booking'))['total_booked']
        if total_booked_tour is None:
            return group_size
        return self.group_size -  total_booked_tour
    
    def get_places_by_cities(self):
        return Place.objects.filter(city__in=self.city.all()).distinct()

    def __str__(self) -> str:
        return str(self.name)
    class Meta:
        ordering = ('created_at',)

# class TourImage(BaseModel)

class TourReview(BaseModel):

    def validate_max_value(value):
        if value > 5:
            raise ValidationError('Value must be equal to or below 5.0.')

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    rate = models.IntegerField(validators=[validate_max_value])
    comment = models.CharField(max_length=100)

    # update hotel rating
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.tour.update_rating(self.tour_id)

    def __str__(self) -> str:
        return str(self.tour.name)

    class Meta:
        ordering = ('created_at',)

class TourBooking(BaseModel):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    email = models.EmailField(max_length=100, blank=True)
    phone_number = models.IntegerField(blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    no_of_people_booking = models.IntegerField()
    total_price = models.IntegerField()
    payment_status = models.BooleanField(default=False)
    cancellation_status = models.BooleanField(default=False)
        
    def __str__(self) -> str:
        return str(self.tour.name)

    class Meta:
        ordering = ('created_at',)

class TourBookingName(BaseModel):
    tour_booking = models.ForeignKey(TourBooking, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self)-> str:
        return str(self.first_name)

class TourImage(BaseModel):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='image/tour/image')


class TourHistoryVisit(BaseModel):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    visit = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.tour.name, self.user.username)
    
    class Meta:
        ordering = ('created_at',)


class TourItinerary(BaseModel):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    itinerary = models.TextField(max_length=2000)