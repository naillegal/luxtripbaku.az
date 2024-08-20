from django.urls import path
from promotion import views


app_name = 'promotion'
urlpatterns = [
    path('', views.home, name='home'),
    path('submit/fleet/', views.submit_fleet_form, name='submit_fleet_form'),
    path('submit/tour/', views.submit_tour_form, name='submit_tour_form'),
    path('updates-request/', views.updates_request_view, name='updates_request'),
    path('tours/', views.tours, name='tours'),
    path('tours/city/<str:city_name>/', views.tours, name='tours_by_city'),
    path('fleet/', views.fleet, name='fleet'),
    path('faq/', views.faq, name='faq'),
    path('contact/', views.contact_request_view, name='contact'),
    path('contact/submit/', views.submit_contact_request, name='contact-submit'),
]