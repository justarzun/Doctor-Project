from django.contrib import admin
from .models import ContactForm , BookingForm
# Register your models here.
admin.site.register(ContactForm)
admin.site.register(BookingForm)