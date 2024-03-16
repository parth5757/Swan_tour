from django.urls import path, include
from app.views import ErrorView
from hotel.views import HotelView
from django.conf import settings
from django.conf.urls.static import static
from tour.views import *
urlpatterns = [
    # the main urls file(all app urls file connected from here)
    path('', include('core.urls')),
    path('hotel/', include('hotel.urls')),
    path('bus/', include('bus.urls')),
    path('tour/', include('tour.urls')),
    path('get_name/', get_name),
    path('<str:undefined_route>/', ErrorView.as_view(), name='error'),
] + static(settings.MEDIA_ROOT, document_root=settings.MEDIA_ROOT)