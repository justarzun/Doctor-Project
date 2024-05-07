from django.forms import ModelForm
import .models import Contact , Booking

class ContactForm(ModelForm):
    class Meta:
        model=Contact
        fields=( 'message','name', 'email', 'subject')

class BookingForm(ModelForm):
    class Meta:
        model=Booking
        fields=( 'name','phone','select', 'email', 'message')