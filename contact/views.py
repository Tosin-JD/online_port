from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Contact, Booking, Testimonial
from django.views.generic import CreateView, DetailView, ListView
from .forms import TestimonyForm, BookingForm


# Create your views here.
class CreateContact(CreateView):
    model = Contact
    fields = ('name', 'email', 'subject', 'message')
    success_url = "home"


class ContactDetail(DetailView):
    model = Contact
    template_name = 'contact/detail_contact.html'
    
    
class ContactList(ListView):
    model = Contact
    template_name = 'contact/list_contacts.html'


class CreateBooking(CreateView):
    model = Booking
    template_name = 'contact/create_booking.html'
    form_class = BookingForm
    success_url = "home"


class BookingDetail(DetailView):
    model = Booking
    template_name = 'contact/detail_booking.html'
    
    
class BookingList(ListView):
    model = Booking
    template_name = 'contact/list_bookings.html'


class CreateTestimony(CreateView):
    model = Testimonial
    form_class = TestimonyForm
    success_url = reverse_lazy("home")
    template_name = 'contact/testimony.html'

