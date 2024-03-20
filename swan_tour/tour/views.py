from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import Tour, TourBooking, TourReview, TourType, TourBookingName, TourImage, TourHistoryVisit
from app.views import BaseView, SuperUserView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, FormView
from django.views.generic import CreateView, TemplateView, ListView
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.contrib import messages 
from bus.models import Bus
from .forms import TourForm, TourBookingNameForm, TourBookingForm, TourImageForm
from hotel.models import Hotel
from core.models import City, Place, State
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
import json
from django.shortcuts import render
from django.http import HttpResponseBadRequest, HttpResponse
from django.views import View
from django.urls import reverse
from django.shortcuts import redirect, get_object_or_404
import datetime
from django.db.models import Q
from django.utils import timezone
from django.forms.models import inlineformset_factory
from .tasks import test_func
import folium
# Create your views here.

class TourListView(SuperUserView, ListView):
    model = Tour
    context_object_name = 'tours'
    template_name = 'tour/tour_list.html'


class TourCreateView(SuperUserView, CreateView):
    model = Tour
    template_name = 'new_tour.html'
    form_class = TourForm
    success_url = reverse_lazy('db_tour_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tourtypes'] = TourType.objects.all()
        print(context['tourtypes'])
        context['cities'] = City.objects.all()
        context['places'] = Place.objects.all()
        context['hotels'] = Hotel.objects.all()
        context['buses'] = Bus.objects.all()
        return context
    
    def form_valid(self, form):
        form.instance.manager = self.request.user
        tour = form.save()

        # save multiple images for tour
        images = self.request.FILES.getlist('images')
        for image in images:
            TourImage.objects.create(tour=tour, image=image)
        messages.success(self.request, "The tour was created successfully.")
        return super().form_valid(form)

    # to check error
    def form_invalid(self, form):
        print(form)
        for error in form.errors:
            print("==> error:", error)
        return super().form_invalid(form)

class TourDeleteView(BaseView, SuperUserView, DeleteView):
    '''Delete view of an Hotel'''
    model = Tour
    template_name = 'tour_list.html'
    success_url = reverse_lazy('tour_list')

    def form_valid(self, form):
        messages.success(self.request, "Tour deleted successfully!!")
        return super().form_valid(form)

# user side tour list with search


class TourUserListView(ListView):
    model = Tour
    context_object_name = 'tours'
    template_name = 'tour/tour_search.html'
    paginate_by = 20

    def get_queryset(self):
        queryset = super().get_queryset()

        # Filter tour_type
        tour_types = self.request.GET.get('tour_type')
        print("tour type: ", tour_types)
        if tour_types:
            tour_type_ids = [int(i) for i in tour_types.split(',')]
            print("tour type: ", tour_type_ids)
            queryset = queryset.filter(tour_type_id__in=tour_type_ids)

        # Filter by ratings
        ratings = self.request.GET.get('ratings')
        if ratings:
            rating_list = ratings.split(",")
            queryset = queryset.filter(rating__in=rating_list)

        # Filter by search name
        search_name = self.request.GET.get('search')
        if search_name:
            # User q objects to make the search case insenstive & match partialstring
            queryset = queryset.filter(Q(name__icontains=search_name))


        # Filter by start date
        start_date = self.request.GET.get('start_date')
        if start_date:
            queryset = queryset.filter(start_date=start_date)

        # Filter by destination (city)
        destination = self.request.GET.get('destination')
        if destination:
            #  queryset = queryset.filter(city__name__icontains=destination)
            queryset = queryset.filter(Q(city__name__icontains=destination) | Q(place__name__icontains=destination)).distinct()



        return queryset

    # city = City.objects.filter(name__contains=query)

    # place = Place.objects.filter(name__contains=query)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tour_count = self.get_queryset().count()
        tour_list = self.get_queryset()

        paginator = Paginator(tour_list, self.paginate_by)
        page = self.request.GET.get('page')
        try:
            tours = paginator.page(page)
        except PageNotAnInteger:
            tours = paginator.page(1)
        except EmptyPage:
            tours = paginator.page(paginator.num_pages)
        tour_types = TourType.objects.all()

        # Pass additional data to the template if needed
        context['search_destination'] = self.request.GET.get('destination', '')
        context['search_start_date'] = self.request.GET.get('start_date', '')

        # Pass the current filters to the template
        context['tour_types'] = tour_types
        # print(tour_types)
        context['tour_count'] = tour_count
        # return all details of t
        context['tours'] = tours
        context['ratings'] = self.request.GET.get('ratings', '')
        context['search_name'] = self.request.GET.get('searh', '')

        return context


class TourDetailView(DetailView):
    model = Tour
    template_name = 'tour/tour_detail.html'
    slug_field = 'tour_slug'  # Specify the model field to use as the slug
    slug_field_kwargs = 'slug'  # Specify the slug field

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tour = self.get_object()

        if tour.start_date <= timezone.now().date():
            message = "Sorry, tour is already in progress or finished"
        else:
            message = None

        context['message'] = message
        # Add the parsed itineraries data to the context
        context['itineraries'] = tour.itineraries
        context['bus_images'] = tour.buses.values_list('bus_image', flat=True)

        # Save visit history if the user is authenticated
        if self.request.user.is_authenticated:
            self.save_visit_history(tour, self.request.user)

        return context

    def save_visit_history(self, tour, user):
        # Check if the user has already visited this tour
        if not TourHistoryVisit.objects.filter(tour=tour, user=user).exists():
            # If not, create a new entry
            visit = TourHistoryVisit(tour=tour, user=user, visit=True)
            visit.save()

        # to hotel image(it example sometime try with python after that use in html template)
        # for i in tour.hotels.all():
        #     print(i.hotel_image)
        #     i.hotel_image


class TourBookingSessionView(BaseView, View):
    def post(self, request, *args, **kwargs):
        # Assuming form data contains 'tour_id' and 'no_of_people_booking'
        tour_id = request.POST.get('tour_id')
        no_of_people_booking = request.POST.get('no_of_people_booking')
        print("tour_id", tour_id)
        # print("no_of_people_booking", no_of_people_booking)

        # Set the session data
        request.session['tour_id'] = tour_id
        request.session['no_of_people_booking'] = no_of_people_booking
        # Redirect to the tour booking page
        return redirect(reverse('tour_booking'))
    
# Single extra form inline form factory
class TourBookingCreateView(BaseView, CreateView):
    model = TourBooking
    template_name = 'tour/tour_booking.html'
    form_class = TourBookingForm
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tour_id = self.request.session.get('tour_id')
        tour = get_object_or_404(Tour, id=tour_id)
        TourBookingNameFormSet = inlineformset_factory(TourBooking, TourBookingName, form=TourBookingNameForm, extra=1)
        if self.request.method == 'POST':
            form = self.form_class(self.request.POST)
            formset = TourBookingNameFormSet(self.request.POST)
        else:
            form = self.form_class()
            formset = TourBookingNameFormSet()
        context['form'] = form
        context['formset'] = formset
        context['tour'] = tour
        context['no_of_people_booking'] = self.request.session.get('no_of_people_booking')
        context['available_group_size'] = tour.get_available_group_size()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if form.is_valid() and formset.is_valid():
            self.object = form.save(commit=False)
            self.object.tour = context['tour']
            self.object.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form))

    def form_invalid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        for error in form.errors:
            print("==> error:", error)

        return self.render_to_response(self.get_context_data(form=form, formset=formset))



# class TourBookingCreateView(CreateView):
#     model = TourBooking
#     template_name = 'tour/tour_booking.html'
#     form_class = TourBookingForm
#     success_url = reverse_lazy('home')

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         tour_id = self.request.session.get('tour_id')
#         tour = get_object_or_404(Tour, id=tour_id)
#         TourBookingNameFormSet = inlineformset_factory(TourBooking, TourBookingName, form=TourBookingNameForm, extra=1, can_delete=True, can_delete_extra=True)

#         # Initialize form and formset with empty data
#         form = self.form_class()
#         formset = TourBookingNameFormSet()

#         context['form'] = form
#         context['formset'] = formset
#         context['tour'] = tour
#         context['no_of_people_booking'] = self.request.session.get('no_of_people_booking')
#         context['available_group_size'] = tour.get_available_group_size()
#         return context

#     def form_valid(self, form):
#         context = self.get_context_data()
#         formset = context['formset']

#         if form.is_valid() and formset.is_valid():
#             self.object = form.save(commit=False)
#             self.object.tour = context['tour']
#             self.object.save()

#             formset.instance = self.object
#             formset.save()

#             return super().form_valid(form)
#         else:
#             return self.render_to_response(self.get_context_data(form=form, formset=formset))

#     def form_invalid(self, form):
#         context = self.get_context_data()
#         formset = context['formset']
#         for error in form.errors:
#             print("==> error:", error)

#         return self.render_to_response(self.get_context_data(form=form, formset=formset))


# api for getting search name of city & place
def get_name(request):  
    search = request.GET.get('search')
    print(search)
    payload = []

    if search:
        city = City.objects.filter(name__icontains = search)
        place = Place.objects.filter(name__icontains = search)

        if city:
            for obj in city:
                payload.append(obj.name)

        if place:
            for obj in place:
                payload.append(obj.name)
        
    return JsonResponse({
        'status': 200,
        'data': payload
    })


# django celery test
def test(request):
    test_func.deleay()
    return HttpResponse("Done")




# Not Working Folium Map inplace that leaft js working
class FoliumView(TemplateView):
    template_name = "tour/map.html"

    # def get_context_data(self, **kwargs):
    #     figure = folium.Figure()
    #     m = folium.Map(
    #         location=[45.372, -121.6972],
    #         zoom_start=12,
    #         tiles='Stamen Terrain'
    #     )
    #     m.add_to(figure)

    #     folium.Marker(
    #         location=[45.3288, -121.6625],
    #         popup='Mt. Hood Meadows',
    #         icon=folium.Icon(icon='cloud')
    #     ).add_to(m)

    #     folium.Marker(
    #         location=[45.3311, -121.7113],
    #         popup='Timberline Lodge',
    #         icon=folium.Icon(color='green')
    #     ).add_to(m)

    #     folium.Marker(
    #         location=[45.3300, -121.6823],
    #         popup='Some Other Location',
    #         icon=folium.Icon(color='red', icon='info-sign')
    #     ).add_to(m)
    #     figure.render()
    #     return {"map": figure}

    # def show_map(request):  
    #     #creation of map comes here + business logic
    #     m = folium.Map([51.5, -0.25], zoom_start=10)
    #     test = folium.Html('<b>Hello world</b>', script=True)
    #     popup = folium.Popup(test, max_width=2650)
    #     folium.RegularPolygonMarker(location=[51.5, -0.25], popup=popup).add_to(m)
    #     m=m._repr_html_() #updated
    #     context = {'my_map': m}

    #     return render(request, 'polls/show_folium_map.html', context)




# to run celery we have 
# celery -A swan_tour.celery worker -l info