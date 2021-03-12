from django import forms
from .models import Testimonial, Booking


class TestimonyForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    
    def __init__(self, *args, **kwargs):
        super(TestimonyForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['class'] = 'form-control my-1'
        self.fields['last_name'].widget.attrs['class'] = 'form-control my-1'
        self.fields['email'].widget.attrs['class'] = 'form-control my-1'
        self.fields['testifier_image'].widget.attrs['class'] = 'form-control my-1'
        self.fields['occupation'].widget.attrs['class'] = 'form-control my-1'
        self.fields['position'].widget.attrs['class'] = 'form-control my-1'
        self.fields['title'].widget.attrs['class'] = 'form-control my-1'
        self.fields['testimony'].widget.attrs['class'] = 'form-control my-1'
        
    class Meta:
        model = Testimonial
        fields = ('first_name', 'last_name', 'email', 'testifier_image', 'occupation', 'position', 'title', 'testimony')



class BookingForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    
    def __init__(self, *args, **kwargs):
        super(BookingForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control my-1'
        self.fields['email'].widget.attrs['class'] = 'form-control my-1'
        self.fields['phone_number'].widget.attrs['class'] = 'form-control my-1'
        self.fields['date'].widget.attrs['class'] = 'form-control my-1'
        self.fields['time'].widget.attrs['class'] = 'form-control my-1'
        self.fields['number_of_people'].widget.attrs['class'] = 'form-control my-1'
        self.fields['message'].widget.attrs['class'] = 'form-control my-1'
        
    class Meta:
        model = Booking
        fields = ('name', 'email', 'phone_number', 'date', 'time', 'number_of_people', 'message')





