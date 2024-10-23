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
    COUNTRY_CHOICES = [
    ('+', '+'),         # Type your own
    ('+994', '+994'),   # Azerbaijan
    ('+968', '+968'),   # Oman
    ('+973', '+973'),   # Bahrain
    ('+965', '+965'),   # Kuwait
    ('+974', '+974'),   # Qatar
    ('+966', '+966'),   # Saudi Arabia
    ('+967', '+967'),   # Yemen
    ('+1', '+1'),       # United States
    ('+44', '+44'),     # United Kingdom
    ('+90', '+90'),     # Turkey
    ('+33', '+33'),     # France
    ('+49', '+49'),     # Germany
    ('+61', '+61'),     # Australia
    ('+81', '+81'),     # Japan
    ('+86', '+86'),     # China
    ('+91', '+91'),     # India
    ('+55', '+55'),     # Brazil
    ('+7', '+7'),       # Russia
    ('+34', '+34'),     # Spain
    ('+39', '+39'),     # Italy
    ('+52', '+52'),     # Mexico
    ('+82', '+82'),     # South Korea
    ('+27', '+27'),     # South Africa
    ('+46', '+46'),     # Sweden
    ('+31', '+31'),     # Netherlands
    ('+45', '+45'),     # Denmark
    ('+47', '+47'),     # Norway
    ('+48', '+48'),     # Poland
    ('+32', '+32'),     # Belgium
    ('+420', '+420'),   # Czech Republic
    ('+41', '+41'),     # Switzerland
    ('+234', '+234'),   # Nigeria
    ('+351', '+351'),   # Portugal
    ('+66', '+66'),     # Thailand
    ('+971', '+971'),   # United Arab Emirates
    ('+92', '+92'),     # Pakistan
    ('+63', '+63'),     # Philippines
    ('+60', '+60'),     # Malaysia
    ('+353', '+353'),   # Ireland
    ('+62', '+62'),     # Indonesia
    ('+64', '+64'),     # New Zealand
    ('+998', '+998'),   # Uzbekistan
]

    country_code = forms.ChoiceField(
        choices=COUNTRY_CHOICES, 
        widget=forms.Select(attrs={'class': 'form-control', 'id': 'country-code'}),
        initial='+994'
    )

    phone_validator = RegexValidator(
        regex=r'^[\d\+\-\(\) ]+$',
        message=_("Phone number must contain only digits and symbols (+, -, (, ), space).")
    )

    phone = forms.CharField(
        validators=[phone_validator],
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'maxlength': '15', 'placeholder': _('Enter your number here')})
    )

    class Meta:
        model = FleetForm
        fields = [
            'pickup_location', 'dropoff_location', 'date_of_service',
            'time_of_service', 'car_class', 'flight_number', 'guest_number',
            'additional_request', 'full_name', 'email', 'country_code', 'phone'
        ]
        widgets = {
            'date_of_service': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'time_of_service': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'guest_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Your guests number here')}),
            'additional_request': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': _('Any additional requests?')}),
            'pickup_location': forms.Select(attrs={'class': 'form-control'}),
            'car_class': forms.Select(attrs={'class': 'form-control'}),
            'dropoff_location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Drop location here')}),
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Type your full name here')}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': _('example@gmail.com')}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'maxlength': '15', 'placeholder': _('Enter your number here')}),
            'flight_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Your flight number here')}),
        }


# TourForm
class TourFormModelForm(forms.ModelForm):
    COUNTRY_CHOICES = [
    ('+', '+'),         # Type your own
    ('+994', '+994'),   # Azerbaijan
    ('+968', '+968'),   # Oman
    ('+973', '+973'),   # Bahrain
    ('+965', '+965'),   # Kuwait
    ('+974', '+974'),   # Qatar
    ('+966', '+966'),   # Saudi Arabia
    ('+967', '+967'),   # Yemen
    ('+1', '+1'),       # United States
    ('+44', '+44'),     # United Kingdom
    ('+90', '+90'),     # Turkey
    ('+33', '+33'),     # France
    ('+49', '+49'),     # Germany
    ('+61', '+61'),     # Australia
    ('+81', '+81'),     # Japan
    ('+86', '+86'),     # China
    ('+91', '+91'),     # India
    ('+55', '+55'),     # Brazil
    ('+7', '+7'),       # Russia
    ('+34', '+34'),     # Spain
    ('+39', '+39'),     # Italy
    ('+52', '+52'),     # Mexico
    ('+82', '+82'),     # South Korea
    ('+27', '+27'),     # South Africa
    ('+46', '+46'),     # Sweden
    ('+31', '+31'),     # Netherlands
    ('+45', '+45'),     # Denmark
    ('+47', '+47'),     # Norway
    ('+48', '+48'),     # Poland
    ('+32', '+32'),     # Belgium
    ('+420', '+420'),   # Czech Republic
    ('+41', '+41'),     # Switzerland
    ('+234', '+234'),   # Nigeria
    ('+351', '+351'),   # Portugal
    ('+66', '+66'),     # Thailand
    ('+971', '+971'),   # United Arab Emirates
    ('+92', '+92'),     # Pakistan
    ('+63', '+63'),     # Philippines
    ('+60', '+60'),     # Malaysia
    ('+353', '+353'),   # Ireland
    ('+62', '+62'),     # Indonesia
    ('+64', '+64'),     # New Zealand
    ('+998', '+998'),   # Uzbekistan
]

    country_code = forms.ChoiceField(
        choices=COUNTRY_CHOICES, 
        widget=forms.Select(attrs={'class': 'form-control', 'id': 'country-code'}),
        initial='+994'
    )
    phone_validator = RegexValidator(
        regex=r'^[\d\+\-\(\) ]+$',
        message=_("Phone number must contain only digits and symbols (+, -, (, ), space).")
    )

    phone = forms.CharField(
        validators=[phone_validator],
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'maxlength': '15', 'placeholder': _('Enter your number here')})
    )

    class Meta:
        model = TourForm
        fields = [
            'select_city', 'planned_tour_days', 'travel_date', 'car_class', 'guest_number',
            'additional_request', 'full_name', 'email', 'country_code', 'phone'
        ]
        widgets = {
            'select_city': forms.SelectMultiple(attrs={'class': 'form-control',}),
            'planned_tour_days': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': _('Number of planned tour days')}),
            'travel_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'car_class': forms.Select(attrs={'class': 'form-control'}),
            'guest_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Your guests number here')}),
            'additional_request': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': _('Any additional requests?')}),
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Type your full name here')}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': _('example@gmail.com')}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'maxlength': '15', 'placeholder': _('Enter your number here')}),
        }