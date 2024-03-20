from django.contrib import admin
from .models import Tour, TourType, TourBooking, TourReview, TourImage, TourHistoryVisit, TourBookingName, TourFacilitys

# Register your models here.

class TourHistoryVisitAdmin(admin.ModelAdmin):
    list_display = ('tour', 'user', 'visit', 'date')

admin.site.register(Tour)
admin.site.register(TourType)
admin.site.register(TourReview)
admin.site.register(TourBooking)
admin.site.register(TourImage)
admin.site.register(TourHistoryVisit)
admin.site.register(TourBookingName)
admin.site.register(TourFacilitys)