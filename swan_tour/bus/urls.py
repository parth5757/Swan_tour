from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import BusView
# from bus.views import 
from app.views import ErrorView


urlpatterns = [
    path('new_bus/', BusView.BusCreateView.as_view(), name="new_bus"),
    path('<str:undefined_router>/', ErrorView.as_view(), name="error")
] + static(settings.MEDIA_ROOT, document_root=settings.MEDIA_ROOT)