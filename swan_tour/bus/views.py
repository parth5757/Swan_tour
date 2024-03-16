from django.shortcuts import render
from app.views import BaseView, SuperUserView
from django.views.generic import CreateView, ListView, TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView, FormView
from core.models import City
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Bus
# Create your views here.

class BusView():
    class BusCreateView(SuperUserView, CreateView):
        model = Bus
        template_name = 'admin/new_bus.html'
        fields = []
        success_url = reverse_lazy('dashboard')

        def form_valid(self, form): 
            form.save()
            return super().form_valid(form)
    
        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['cities']= City.objects.all()
            # context['placies'] = Place.objects.all()
            return context
        
    
        # class BusListView()