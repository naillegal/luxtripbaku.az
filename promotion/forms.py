from django import forms
from .models import City
from .models import ContactRequest, UpdatesRequest, FleetForm, TourForm
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

# Tour Select City Form


class CityFilterForm(forms.Form):
    city = forms.ChoiceField(
        choices=[('', 'All')],
        required=False,
        widget=forms.Select(attrs={'id': 'city-filter'})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        cities = City.objects.all()
        if cities:
            city_choices = [(city.name, city.name) for city in cities]
            self.fields['city'].choices += city_choices
        else:
            self.fields['city'].choices = [('', 'All')]


# Contact Form
class ContactRequestForm(forms.ModelForm):
    phone_validator = RegexValidator(
        regex=r'^[\d\+\-\(\) ]+$',
        message=_("Phone number must contain only digits and symbols (+, -, (, ), space).")
    )

    phone = forms.CharField(
        validators=[phone_validator],
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': _('Phone')})
    )

    class Meta:
        model = ContactRequest
        fields = ['name', 'email', 'phone', 'website', 'additional_request']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Name')}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': _('Email')}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Phone')}),
            'website': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Website')}),
            'additional_request': forms.Textarea(attrs={'class': 'form-control', 'placeholder': _('Additional request'), 'rows': 3}),
        }

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        additional_request = cleaned_data.get('additional_request')

        if not name:
            self.add_error('name', _("You need to type your name."))
        if not additional_request:
            self.add_error('additional_request',
                           _("You need to type your request."))


# UpdatesRequestForm
class UpdatesRequestForm(forms.ModelForm):
    class Meta:
        model = UpdatesRequest
        fields = ['email']


# FleetForm
class FleetFormModelForm(forms.ModelForm):
    phone_validator = RegexValidator(
        regex=r'^[\d\+\-\(\) ]+$',
        message=_("Phone number must contain only digits and symbols (+, -, (, ), space).")
    )

    phone = forms.CharField(
        validators=[phone_validator],
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': '+'})
    )

    class Meta:
        model = FleetForm
        fields = [
            'pickup_location', 'dropoff_location', 'date_of_service',
            'time_of_service', 'car_class', 'flight_number',
            'additional_request', 'full_name', 'email', 'phone'
        ]
        widgets = {
            'date_of_service': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'time_of_service': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'additional_request': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': _('Any additional requests?')}),
            'pickup_location': forms.Select(attrs={'class': 'form-control'}),
            'car_class': forms.Select(attrs={'class': 'form-control'}),
            'dropoff_location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Drop location here')}),
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Type your full name here')}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': _('example@gmail.com')}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+'}),
            'flight_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Your flight number here')}),
        }


# TourForm
class TourFormModelForm(forms.ModelForm):
    phone_validator = RegexValidator(
        regex=r'^[\d\+\-\(\) ]+$',
        message=_("Phone number must contain only digits and symbols (+, -, (, ), space).")
    )

    phone = forms.CharField(
        validators=[phone_validator],
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': '+'})
    )

    class Meta:
        model = TourForm
        fields = [
            'select_city', 'planned_tour_days', 'travel_date', 'car_class',
            'additional_request', 'full_name', 'email', 'phone'
        ]
        widgets = {
            'select_city': forms.SelectMultiple(attrs={'class': 'form-control',}),
            'planned_tour_days': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': _('Number of planned tour days')}),
            'travel_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'car_class': forms.Select(attrs={'class': 'form-control'}),
            'additional_request': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': _('Any additional requests?')}),
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Type your full name here')}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': _('example@gmail.com')}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+'}),
        }