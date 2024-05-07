from django.shortcuts import render
from django.http import HttpResponse
from . models import ContactForm , BookingForm
# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def blog(request):
    return render(request, 'blog.html')

def services(request):
    return render(request, 'services.html')      

def contactform(request):
    if request.method == "POST":
        msg = request.POST.get("c_message")
        nam = request.POST.get("c_name")
        em = request.POST.get("c_email")
        sub = request.POST.get("c_subject")
        
        abc = ContactForm( message=msg, name=nam, email=em, subject=sub)
        abc.save()
        return HttpResponse("<h4>DATA SENT SUCCESSFULLY</h4>")
    else:
        return render(request,'index.html')


def bookingform(request):
    if request.method == "POST":
        nm = request.POST.get("b_name")
        phn = request.POST.get("b_phone")
        sel= request.POST.get("b_select")
        ema = request.POST.get("b_email")
        mes = request.POST.get("b_message")
        
        xyz = BookingForm(name=nm, phone=phn, select=sel,email=ema, message=mes)
        xyz.save()
        return HttpResponse("<h4>DATA SENT SUCCESSFULLY</h4>")
    else:
        return render(request,'index.html')      