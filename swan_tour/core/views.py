from django.db.models.query import QuerySet
from .forms import ContactForm, CustomPasswordChangeForm
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from app.views import BaseView
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeDoneView, PasswordChangeView
from django.views.generic import CreateView, ListView, TemplateView, View
from django.views.generic.edit import UpdateView, DeleteView, FormView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.contrib.auth.views import LoginView
from app.views import SuperUserView,BaseView
from core.models import Contact, Place, City, State
from hotel.models import Hotel
from tour.models import Tour, TourType, TourBooking, TourHistoryVisit, TourImage
from django.db.models import Count
from bus.models import Bus
from django_datatables_too.mixins import DataTableMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django_datatables_view.base_datatable_view import BaseDatatableView


from django.contrib.auth.views import PasswordChangeView


# Create your views here.

class UserView():

    class MyLoginView(LoginView):
        redirect_authenticated_user = True

        def get_success_url(self):
            if self.request.user.is_superuser == True:
                return reverse_lazy('dashboard')
            else:
                return reverse_lazy('home')
        
        def form_invalid(self, form):
            messages.error(self.request, 'invalid username or password')
            return self.render_to_response(self.get_context_data(form=form))

    class RegisterUser(CreateView):
        '''Create at User Registration'''
        model = User #model name
        template_name = 'users/register.html'
        fields = ["first_name", "last_name", "username", "email", "password", "is_active"] #field that want to send from user
        success_url = reverse_lazy('login')
        
        '''check form is valid or not if valid than executr'''
        def form_valid(self, form):
            form.instance.password = make_password(form.cleaned_data['password'])
            form.save()
            return super().form_valid(form)
        
        # to check error
        # def form_invalid(self, form):
        #     for error in form.errors:
        #         print("==> error:", error)
        #     return super().form_invalid(form)


    class Place(ListView):
        model = Place
        template_name = 'admin/places.html'
        context_object_name = 'place'

        def get_queryset(self):
            queryset = super().get_queryset()

            # Filter by destination (city or place)
            destination = self.request.GET.get('destination')

            if destination:
                # You can combine queries for both City and Place using Q objects
                from django.db.models import Q
                queryset = queryset.filter(Q(city__name__icontains=destination) | Q(place__name__icontains=destination))

            return queryset

    class PlaceListJson(BaseDatatableView):
        model = Place
        columns = ['id', 'name', 'city']
        order_columns = ['id', 'name', 'city']

        def render_column(self, row, column):
            # We want to render the city name instead of its ID
            if column == 'city':
                return row.city.name
            else:
                return super().render_column(row, column)

        def filter_queryset(self, qs):
            # If there are filters applied, filter the queryset accordingly
            search_value = self.request.GET.get('search[value]', None)
            if search_value:
                qs = qs.filter(name__icontains=search_value) | qs.filter(city__name__icontains=search_value)
            return qs

        def get_initial_queryset(self):
            # Return the initial queryset of all places
            return Place.objects.all()

    class AddPlace(SuperUserView, CreateView):
        model = Place
        template_name = 'admin/new_place.html'
        fields = ['name', 'city', 'image']
        success_url = reverse_lazy('place_list')

        def form_valid(self, form):
            form.save()
            return super().form_valid(form)

        def form_invalid(self, form):
            # print(form)
            for error in form.errors:
                print("==> error:", error)
            return super().form_invalid(form)

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['cities']= City.objects.all()
            return context
    
    class PlaceDeleteView(SuperUserView, DeleteView):
        model = Place
        template_name = 'admin/places.html'
        success_url = reverse_lazy('place')

        def form_vaid(self, form):
            messages.success(self.request, "Placfcitye has been deleted successfully")
            return super().form_valid(form)


    class AddCity(SuperUserView, CreateView):
        model = City
        template_name = 'admin/new_city.html'
        fields = ['name', 'state', 'image', 'location']
        success_url = reverse_lazy('dashboard')

        def form_valid(self, form):
            print(form)
            form.save()
            return super().form_valid(form)
        
        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['states']= State.objects.all()
            return context
        
                # to check error
        def form_invalid(self, form):
            # print(form)
            for error in form.errors:
                print("==> error:", error)
            return super().form_invalid(form)

    class City(ListView, SuperUserView):
        model = City
        context_object_name = 'city'
        template_name = 'admin/city.html'

    class CityListJson(BaseDatatableView):
        model = City
        columns = ['id', 'name','state']
        order_columns = ['id', 'name','state']

        def render_column(self, row, column):
            # We want to render the city name instead of its ID
            if column =='state':
                return row.state.name
            else:
                return super().render_column(row, column)

        def filter_queryset(self, qs):
            search_value = self.request.GET.get('search[value]', None)
            if search_value:
                qs = qs.filter(name_icontains=search_value) | qs.filter(state__name__icontains=search_value)
            return qs

        def get_initial_queryset(self):
            return City.objects.all()

    class CityDeleteView(SuperUserView, DeleteView):
        model = City
        template_name = 'admin/city.html'
        success_url = reverse_lazy('city')

        def form_vaid(self, form):
            messages.success(self.request, "city has been deleted successfully")
            return super().form_valid(form)

    # class Home(TemplateView):

    #     # Create at Home View return home page 
    #     template_name = 'common/index.html'
    #     queryset = Hotel.objects.none()
    #     def get_context_data(self, **kwargs):
    #         context = super().get_context_data(**kwargs)

    #         # return some of top trending packages (return last 5 tour book)
    #         all_tour = TourType.objects.all()
    #         tours = Tour.objects.order_by('-created_at')[:6]
    #         # Retrive popula places
    #         # popular_places = Place.objects.annotate(num_tour=Count('tour')).order_by('-num_tours')[:5]

    #         total_place = Place.objects.all()
    #         place_len = len(total_place)
    #         popular_places = Place.objects.all()
            
    #         # recive top hotels
    #         total_hotel = Hotel.objects.all()
    #         hotel_len = len(total_hotel)
    #         top_hotel = Hotel.objects.order_by('-rating')[:5]
    #         # partners = total_hotel.hotel_image

    #         # context['hot_tours'] = hot_tours

    #         context['popular_places'] = popular_places
    #         context['tours'] = tours
    #         context['top_hotel'] = top_hotel
    #         context['place_len'] = place_len
    #         context['hotel_len'] = hotel_len
    #         context['all_tour'] = all_tour

    #         context['total_hotel'] = total_hotel
    #         return context



    class Home(TemplateView):
        template_name = 'common/index.html'

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)

            # Get top trending packages (last 6 tours)
            tours = Tour.objects.order_by('-created_at')[:6]

            # Retrieve popular places
            popular_places = Place.objects.order_by('-created_at')[:20  ]  # You need to define Place model

            # Retrieve top hotels
            top_hotel = Hotel.objects.order_by('-rating')[:5]
            total_place = Place.objects.all()
            place_len = len(total_place)
            total_hotel = Hotel.objects.all()
            hotel_len = len(total_hotel)

            # Check if the user is authenticated
            if self.request.user.is_authenticated:
                # Retrieve recent tour history for the authenticated user
                recent_tours = TourHistoryVisit.objects.filter(user=self.request.user, visit=True).order_by('-date')[:2]
                recent_tour_ids = [visit.tour.id for visit in recent_tours]

                # Exclude recently visited tours from the main tour queryset
                excluded_tours = Tour.objects.filter(id__in=recent_tour_ids)
                remaining_tours_count = 6 - len(recent_tour_ids)
                remaining_tours = Tour.objects.exclude(id__in=recent_tour_ids)[:remaining_tours_count]

                # Concatenate both lists to display on the homepage
                final_tours = list(excluded_tours) + list(remaining_tours)

                context['recent_tours'] = final_tours
            else:
                # If user is not authenticated, show regular tours
                context['tours'] = tours

            context['popular_places'] = popular_places
            context['top_hotel'] = top_hotel
            context['hotel_len'] = hotel_len
            context['place_len'] = place_len
            return context


class Profile(LoginRequiredMixin, TemplateView):
        template_name = 'users/my_profile.html'

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            user = self.request.user
            context['user'] = user
            return context

class Dashboard(SuperUserView, BaseView, TemplateView):
    '''creat admin home page'''
    template_name = 'admin/db_dashboard.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total_number_place = Place.objects.count()
        total_number_hotel = Hotel.objects.count()
        total_number_tour = Tour.objects.count()
        total_number_bus = Bus.objects.count()
        context['tourbooking'] = TourBooking.objects.all()[:6]
        context['bookings'] = TourBooking.objects.all()
        context['total_number_place'] = total_number_place
        context['total_number_hotel'] = total_number_hotel
        context['total_number_tour'] =total_number_tour
        context['total_number_bus'] =total_number_bus
        return context
    
class About(TemplateView):
    template_name = "common/about.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total_number_place = Place.objects.count()
        total_number_hotel = Hotel.objects.count()
        total_number_tour = Tour.objects.count()
        total_number_booking = TourBooking.objects.count()
        context['total_number_place'] = total_number_place
        context['total_number_hotel'] = total_number_hotel
        context['total_number_tour'] = total_number_tour
        context['total_number_booking'] = total_number_booking
        return context

class Contact (CreateView):
    model = Contact
    template_name = "common/contact.html"
    # form = ContactForm
    fields = "__all__"
    success_url = reverse_lazy('send_contact_mail')
    
    def form_valid(self, form):
        form.save()
        
        return super().form_valid(form)
    
            # to check error
    def form_invalid(self, form):
        for error in form.errors:
            print("==> error:", error)
        return super().form_invalid(form)
    

class ContactNotification(TemplateView):
    template_name = "common/db_notification.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        contacts = Contact.objects.all()
        context['contacts'] = contacts
        return context
    

class CustomPasswordChangeView(PasswordChangeView):
    form_class = CustomPasswordChangeForm  # Use the custom form
    template_name = 'users/my_profile.html'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        messages.success(self.request, 'Your password has been changed successfully.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'There was an error. Please try again.')
        return super().form_invalid(form)
