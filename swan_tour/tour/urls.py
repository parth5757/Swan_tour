from django.urls import path, include
from .views import TourListView, TourCreateView, TourDetailView, TourUserListView, TourBookingSessionView, TourBookingCreateView, FoliumView, RepeatTourCreateView, TourUpdateView, TourReviewCreateView, TourDeleteView
from app.views import ErrorView
from django.conf import settings
from django.conf.urls.static import static
# from tour.views import *
from . import views

urlpatterns = [
    #  tour admin side table view
    path('db_tour_list', TourListView.as_view(), name='db_tour_list'),
    # adding new tour admin side table view
    path('new_tour', TourCreateView.as_view(), name='new_tour' ),
    path('add_repeat_tour', RepeatTourCreateView.as_view(), name='add_repeat_tour'),
    path('tour_update/<int:pk>', TourUpdateView.as_view(), name='tour_update'),
    path('tour_delete/<int:pk>', TourDeleteView.as_view(), name='tour_delete'),
    path('tour_search/', TourUserListView.as_view(), name='tour_user_list'),
    path('tour_detail/<slug:slug>', TourDetailView.as_view(), name='tour_detail'),
    # tour booking sessions
    path('tour_booking_session/<slug:slug>', TourBookingSessionView.as_view(), name='tour_booking_session'),
    path('tour_booking/', TourBookingCreateView.as_view(), name='tour_booking'),
    path('tour_review/', TourReviewCreateView.as_view(), name='tour_review'),
    path('<str:undefined_route>/', ErrorView.as_view(), name='error'),
    path('map', FoliumView.as_view(), name='map'),
    path('send_mail', views.send_contact_response, name="send_contact_mail"),
] + static(settings.MEDIA_ROOT, document_root=settings.MEDIA_ROOT)