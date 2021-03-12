from django.urls import path
from .views import (CreateContact, 
                    ContactDetail,
                    ContactList,
                    CreateTestimony,
                    BookingList,
                    BookingDetail,
                    CreateBooking,
                    TestimonyForm)
                    
                    
                    
app_name = "contact"

urlpatterns = [
    path('', CreateContact.as_view(), name='create'),
    path('create-booking/', CreateBooking.as_view(), name='book'),
    path('list/', ContactList.as_view(), name='list'),
    path('bookings/', BookingList.as_view(), name='b_list'),
    path('<int:pk>/', ContactDetail.as_view(), name='detail'),
    path('<int:pk>/bkng/', BookingDetail.as_view(), name='b_detail'),
    path('testimony/', CreateTestimony.as_view(), name='testimony'),
    
    ]
