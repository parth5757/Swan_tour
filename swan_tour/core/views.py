from django.db.models.query import QuerySet
from .forms import ContactForm
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from app.views import BaseView
from django.contrib.auth.models import User
from django.views.generic import CreateView, ListView, TemplateView, View
from django.views.generic.edit import UpdateView, DeleteView, FormView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.contrib.auth.views import LoginView
from app.views import SuperUserView,BaseView
from core.models import Place, City, State, Contact
from hotel.models import Hotel
from tour.models import Tour, TourType, TourBooking
from django.db.models import Count
from bus.models import Bus
from django_datatables_too.mixins import DataTableMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django_datatables_view.base_datatable_view import BaseDatatableView
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
        fields = ["first_name", "last_name", "username", "email", "password"] #field that want to send from user
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
        fields = ['name', 'state', 'image']
        success_url = reverse_lazy('dashboard')

        def form_valid(self, form):
            form.save()
            return super().form_valid(form)
        
        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['states']= State.objects.all()
            return context

    class City(ListView, SuperUserView):
        model = City
        context_object_name = 'city'
        template_name = 'admin/city.html'


    class CityDeleteView(SuperUserView, DeleteView):
        model = City
        template_name = 'admin/city.html'
        success_url = reverse_lazy('city')

        def form_vaid(self, form):
            messages.success(self.request, "city has been deleted successfully")
            return super().form_valid(form)

    class Home(TemplateView):

        # Create at Home View return home page 
        template_name = 'common/index.html'
        queryset = Hotel.objects.none()
        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)

            # return some of top trending packages (return last 5 tour book)
            all_tour = TourType.objects.all()
            tours = Tour.objects.order_by('-created_at')[:6]
            # Retrive popula places
            # popular_places = Place.objects.annotate(num_tour=Count('tour')).order_by('-num_tours')[:5]

            total_place = Place.objects.all()
            place_len = len(total_place)
            popular_places = Place.objects.all()
            
            # recive top hotels
            total_hotel = Hotel.objects.all()
            hotel_len = len(total_hotel)
            top_hotel = Hotel.objects.order_by('-rating')[:5]
            # partners = total_hotel.hotel_image

            # context['hot_tours'] = hot_tours

            context['popular_places'] = popular_places
            context['tours'] = tours
            context['top_hotel'] = top_hotel
            context['place_len'] = place_len
            context['hotel_len'] = hotel_len
            context['all_tour'] = all_tour

            context['total_hotel'] = total_hotel
            return context

class Profile(LoginRequiredMixin, TemplateView):
        template_name = 'users/my_profile.html'

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            user = self.request.user
            context['user'] = user
            print("email", user.email)
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
        context['total_number_place'] = total_number_place
        context['total_number_hotel'] = total_number_hotel
        context['total_number_tour'] =total_number_tour
        context['total_number_bus'] =total_number_bus
        return context
    
class About(TemplateView):
    template_name = "common/about.html"


class Contact (CreateView):
    model = Contact
    template_name = "common/contact.html"
    # form = ContactForm
    fields = "__all__"
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
            # to check error
    def form_invalid(self, form):
        for error in form.errors:
            print("==> error:", error)
        return super().form_invalid(form)
    


