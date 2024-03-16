from django.db import models
from app.models import BaseModel
from core.models import City, Place
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

# Create your models here.
class Bus(BaseModel):

    name = models.CharField(max_length=50)
    bus_number = models.IntegerField()
    price = models.IntegerField()
    rating =models.FloatField(null=True, default=0)
    facility = models.CharField(max_length=100)
    overview = models.CharField(max_length=500)
    seat = models.CharField(max_length=100, blank=True, null=True)
    start_point_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='start_point_buses')
    end_point_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='end_point_buses')
    bus_company_image = models.ImageField(upload_to='image/bus/')
    bus_image = models.ImageField(upload_to='image/bus/')


    @classmethod
    def update_rating(cls, bus_id):
        bus = cls.objects.get(id=bus_id)
        reviews = Bus_Review.objects.filter(bus_id=bus_id)
        average_rating = reviews.aggregate(models.Avg('rate'))['rate__avg']
        if average_rating is None:
            average_rating = 0


    def __str__(self) -> str:
        return str(self.name)

    class Meta:
        ordering = ('created_at',)


class Bus_Review(BaseModel):
    
    def validate_max_value(value):
        if value > 5:
            raise ValidationError('Value must be equal to or below 5.0.')

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    rate = models.IntegerField(validators=[validate_max_value])
    comment = models.CharField(max_length=100)

    # update hotel rating
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.bus.update_rating(self.bus_id)
        
    def __str__(self) -> str:
        return str(self.bus.name)

    class Meta:
        ordering = ('created_at',)


class TourBus(BaseModel):
    name = models.CharField(max_length=50)
    bus_number = models.IntegerField()
    price = models.IntegerField()