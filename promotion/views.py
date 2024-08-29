from django.shortcuts import render, redirect
from .models import Tour, Car, Faq, HomeFirstContent, Whoweare
from .forms import CityFilterForm, ContactRequestForm, UpdatesRequestForm, FleetFormModelForm, TourFormModelForm
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.


def home(request):
    first_content = HomeFirstContent.objects.all()
    whoweare_content = Whoweare.objects.first()

    fleetform = FleetFormModelForm(prefix='fleet_')
    tourform = TourFormModelForm(prefix='tour_')

    if 'fleet_submit' in request.GET:
        if request.GET.get('fleet_submit') == 'success':
            messages.success(
                request, 'Your request has been sent! Thank you for choosing us!')
        elif request.GET.get('fleet_submit') == 'error':
            messages.error(
                request, 'Fleet form submission failed. Please correct the errors.')

        fleetform = FleetFormModelForm(prefix='fleet_')

    if 'tour_submit' in request.GET:
        if request.GET.get('tour_submit') == 'success':
            messages.success(
                request, 'Your tour request has been sent! Thank you for choosing us!')
        elif request.GET.get('tour_submit') == 'error':
            messages.error(
                request, 'Tour form submission failed. Please correct the errors.')

        tourform = TourFormModelForm(prefix='tour_')

    return render(request, 'index.html', {
        'first_content': first_content,
        'whoweare': whoweare_content,
        'fleetform': fleetform,
        'tourform': tourform,
    })


def submit_fleet_form(request):
    if request.method == 'POST':
        fleetform = FleetFormModelForm(request.POST, prefix='fleet_')
        if fleetform.is_valid():
            fleetform.save()
            send_mail(
                'You have a new Transfer Form',  
                'Details are available in the admin panel.', 
                settings.EMAIL_HOST_USER,  
                ['luxtripbaku@gmail.com'],  
                fail_silently=False,
            )
            messages.success(
                request, 'Your transfer request has been sent! Thank you for choosing us!')
            return redirect('/')
        else:
            messages.error(
                request, 'Transfer form submission failed. Please correct the errors.')
            return render(request, 'index.html', {
                'fleetform': fleetform,
                'tourform': TourFormModelForm(prefix='tour_'),
                'first_content': HomeFirstContent.objects.all()
            })
    return redirect('/')


def submit_tour_form(request):
    if request.method == 'POST':
        tourform = TourFormModelForm(request.POST, prefix='tour_')
        if tourform.is_valid():
            tourform.save()
            send_mail(
                'You have a new Tour Form',  
                'Details are available in the admin panel.', 
                settings.EMAIL_HOST_USER,  
                ['luxtripbaku@gmail.com'],  
                fail_silently=False,
            )
            messages.success(
                request, 'Your tour request has been sent! Thank you for choosing us!')
            return redirect('/')
        else:
            messages.error(
                request, 'Tour form submission failed. Please correct the errors.')
            return render(request, 'index.html', {
                'fleetform': FleetFormModelForm(prefix='fleet_'),
                'tourform': tourform,
                'first_content': HomeFirstContent.objects.all()
            })
    return redirect('/')


def updates_request_view(request):
    if request.method == 'POST':
        form = UpdatesRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UpdatesRequestForm()

    return render(request, 'index.html', {'form': form})


def tours(request):
    form = CityFilterForm(request.GET or None)
    tours = Tour.objects.all()
    fleetform = FleetFormModelForm(prefix='fleet_')
    tourform = TourFormModelForm(prefix='tour_')

    if 'fleet_submit' in request.GET:
        if request.GET.get('fleet_submit') == 'success':
            messages.success(
                request, 'Your request has been sent! Thank you for choosing us!')
        elif request.GET.get('fleet_submit') == 'error':
            messages.error(
                request, 'Fleet form submission failed. Please correct the errors.')

        fleetform = FleetFormModelForm(prefix='fleet_')

    if 'tour_submit' in request.GET:
        if request.GET.get('tour_submit') == 'success':
            messages.success(
                request, 'Your tour request has been sent! Thank you for choosing us!')
        elif request.GET.get('tour_submit') == 'error':
            messages.error(
                request, 'Tour form submission failed. Please correct the errors.')

        tourform = TourFormModelForm(prefix='tour_')

    if form.is_valid():
        city_name = form.cleaned_data.get('city')
        if city_name:
            tours = tours.filter(city__name=city_name)

    context = {
        'tours': tours,
        'form': form,
        'fleetform': fleetform,
        'tourform': tourform,
    }
    return render(request, 'tours.html', context)


def fleet(request):
    cars = Car.objects.all()
    fleetform = FleetFormModelForm(prefix='fleet_')
    tourform = TourFormModelForm(prefix='tour_')

    if 'fleet_submit' in request.GET:
        if request.GET.get('fleet_submit') == 'success':
            messages.success(
                request, 'Your request has been sent! Thank you for choosing us!')
        elif request.GET.get('fleet_submit') == 'error':
            messages.error(
                request, 'Fleet form submission failed. Please correct the errors.')

        fleetform = FleetFormModelForm(prefix='fleet_')

    if 'tour_submit' in request.GET:
        if request.GET.get('tour_submit') == 'success':
            messages.success(
                request, 'Your tour request has been sent! Thank you for choosing us!')
        elif request.GET.get('tour_submit') == 'error':
            messages.error(
                request, 'Tour form submission failed. Please correct the errors.')

        tourform = TourFormModelForm(prefix='tour_')

    context = {
        'cars': cars,
        'fleetform': fleetform,
        'tourform': tourform
    }
    return render(request, 'fleet.html', context)


def faq(request):
    faqs = Faq.objects.all()
    return render(request, 'faq.html', {'faqs': faqs})


def contact_request_view(request):
    form = ContactRequestForm()
    if request.method == 'GET' and 'submit' in request.GET:
        if request.GET.get('submit') == 'success':
            messages.success(request, "Your request has been sent!")
        elif request.GET.get('submit') == 'error':
            messages.error(request, "Your request could not be sent!")

    return render(request, 'contact.html', {'form': form})


def submit_contact_request(request):
    if request.method == 'POST':
        form = ContactRequestForm(request.POST)
        if form.is_valid():
            form.save()
            send_mail(
                'You have a new Contact Form',  
                'Details are available in the admin panel.', 
                settings.EMAIL_HOST_USER,  
                ['luxtripbaku@gmail.com'],  
                fail_silently=False,
            )
            return redirect('/contact?submit=success')
        else:
            for errors in form.errors.items():
                for error in errors:
                    messages.error(request, error)
            return redirect('/contact?submit=error')
    return redirect('/contact')
