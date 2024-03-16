from django.contrib import admin
from .models import Hotel, Hotel_Review, Hotel_Booking
from core.models import State, City
# Register your models here.

class HotelAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "city":
            state_id = request.POST.get('state')
            kwargs["queryset"] = City.objects.filter(state_id=state_id)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
class HotelBookingAdmin(admin.ModelAdmin):
    list_display =('user', 'hotel', 'first_name', 'last_name', 'valid_date_from', 'valid_date_till', 'no_room_booking', 'total_price')

admin.site.register(Hotel)
admin.site.register(Hotel_Review)
admin.site.register(Hotel_Booking)