from django.urls import path, include
from .views import UserView
from app.views import ErrorView
from .views import UserView, About, Dashboard, Contact, Profile, ContactNotification, CustomPasswordChangeView
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth.views import (
    LogoutView,
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView,
    PasswordResetCompleteView
)


urlpatterns = [

    # login register logout
    path('login/', UserView.MyLoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', UserView.RegisterUser.as_view(), name='register'),


    # forget password
    path('password-reset/', PasswordResetView.as_view(template_name='users/password_reset.html'),name='password-reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='users/reset_password_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/',PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),name='password_reset_complete'),
    

    path('change_password/', CustomPasswordChangeView.as_view(), name='change_password'),


    # path()
    path('profile/', Profile.as_view(), name='profile'),
    path('', UserView.Home.as_view(), name='home'),
    path('about/', About.as_view(), name='about'),
    path('contact/', Contact.as_view(), name='contact'),
    path('notification/', ContactNotification.as_view(), name='notification'),

    # addmin sid urls
    path('dashboard/', Dashboard.as_view(), name='dashboard'),

    # place url
    path('add_place/', UserView.AddPlace.as_view(), name='add_place'),
    path('place/', UserView.Place.as_view(), name='place_list'),
    path('place/list/json/', UserView.PlaceListJson.as_view(), name='place_list_json'),
    path('delete_place/<int:pk>', UserView.PlaceDeleteView.as_view(), name='place_delete'),
    
    # city urls
    path('add_city/', UserView.AddCity.as_view(), name='add_city'),
    path('city/', UserView.City.as_view(),name="city"),
    path('city/list/json', UserView.CityListJson.as_view(), name='city_list_json'),
    path('delete_city/<int:pk>', UserView.CityDeleteView.as_view(), name='city_delete'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT   )