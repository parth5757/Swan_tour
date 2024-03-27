from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import Hotel, Hotel_Review, HotelBooking, HotelImage
from django.views.generic import CreateView, ListView, TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.models import User
from app.views import BaseView, SuperUserView
from .forms import HotelForm
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views import View
from core.models import City, Place
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
# Create your views here.

class HotelView():

    class HotelCreateView(BaseView, SuperUserView, CreateView):
        model = Hotel
        # form_class = HotelForm
        template_name = 'hotel/db_vendor_add_hotel.html'
        fields = ['hotelname', 'address', 'map_link', 'total_room', 'price', 'rating', 'overview', 'facility', 'city', 'place']
        success_url = reverse_lazy('db_hotel_list')
        
        def form_valid(self, form): 
            form.instance.manager = self.request.user
            hotel = form.save()

            # save multiple images for tour
            images = self.request.FILES.getlist('images')
            for image in images:
                HotelImage.objects.create(hotel=hotel, image=image)
            messages.success(self.request, "The Hotel was created successfully.")
            
            return super().form_valid(form)
        
        # to check error
        def form_invalid(self, form):
            # print(form)
            for error in form.errors:
                print("==> error:", error)
            return super().form_invalid(form)
    
        
        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['cities']= City.objects.all()
            context['placies'] = Place.objects.all()
            return context


    class HotelListView(BaseView, SuperUserView, ListView):
        model =Hotel
        context_object_name = 'hotel'
        template_name = 'hotel/db_vendor_hotels.html'
    
        # add hotel search option
        # def get_queryset(self):
        #     search = self.request.GET.get('search', '')
        #     hotel = Hotel.objects.filter(first_name_locations=search)
        #     return hotel

    class HotelDeleteView(BaseView, SuperUserView, DeleteView):
        '''Delete view of an Hotel'''
        model = Hotel
        template_name = 'hotel/db_vendor_hotels.html'
        success_url = reverse_lazy('db_hotel_list')

        def form_valid(self, form):
            messages.success(self.request, "Hotel deleted successfully!!")
            return super().form_valid(form)
        
    class HotelUpdateView(BaseView, SuperUserView, UpdateView):
        '''Hotel Updat view'''
        model = Hotel
        fields = ['hotelname', 'address', 'total_room', 'price', 'facility']
        template_name = 'hotel/hotel_update.html'
        success_url = reverse_lazy('db_hotel_list')


    class HotleBookingListView(SuperUserView, ListView):
        model = HotelBooking
        context_object_name = 'hotel_booking'
        template_name = 'hotel/hotel_booking_list.html'

class HotelUserView():

    class HotelListView(ListView):
        model = Hotel
        context_object_name = 'hotel'
        template_name = 'hotel/hotel_user_list.html'
        paginate_by = 6

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            hotel_count = Hotel.objects.count()
            hotel_list = Hotel.objects.all()

            paginator = Paginator(hotel_list, self.paginate_by)
            page = self.request.GET.get('page')

            try:
                hotel1 = paginator.page(page)
            except PageNotAnInteger:
                # If the page argument isn't an integer, deliver the first page.
                hotel1 = paginator.page(1)
            except EmptyPage:
                # If page is out of range, deliver last page of results.
                hotel1 = paginator.page(paginator.num_pages)
            
            context['hotel_count'] = hotel_count
            context['hotel1'] = hotel1
            return context

        # def get_context_data(self, **kwargs):
        #     context = super().get_context_data(**kwargs)
        #     hotel_count = Hotel.objects.count()
        #     hotel = Hotel.objects.all()
        #     context['hotel_count'] = hotel_count
        #     context['hotel'] = hotel
        #     return context


    class HotelDetailView(DetailView):
        model = Hotel



    class ReviewCreate(BaseView, CreateView):
        model = Hotel_Review    
        template_name = 'hotel/hotel_booking.html'
        fields = ['user', 'hotel', 'rate', 'comment']
        success_url = reverse_lazy('db_hotel_list')


    class UserHotelView(BaseView, TemplateView):
        model = Hotel
        context_object_name = 'hotel'
        template_name = 'hotel_booking.html'

