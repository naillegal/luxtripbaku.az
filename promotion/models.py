from django.db import models

# Create your models here.

# Tour Model 
class City(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False, verbose_name='City name')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')
    updated = models.DateTimeField(auto_now=True, verbose_name='Last Updated')

    class Meta:
        ordering = ['-created']
        verbose_name = 'City'
        verbose_name_plural = 'City'

    def __str__(self):
        return self.name

class Tour(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False, verbose_name='Tour name')
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='tours')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')
    updated = models.DateTimeField(auto_now=True, verbose_name='Last Updated')

    class Meta:
        ordering = ['-created']
        verbose_name = 'Add Tours'
        verbose_name_plural = 'Add Tours'

    def __str__(self):
        return self.title
    
class TourImage(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='tours/',null=False, blank=False, verbose_name='Tour image')
    caption = models.CharField(max_length=255,null=True, blank=True, verbose_name='Image caption')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')
    updated = models.DateTimeField(auto_now=True, verbose_name='Last Updated')

    class Meta:
        ordering = ['-created']
        verbose_name = 'Tour images'
        verbose_name_plural = 'Tour images'

    def __str__(self):
        return self.caption or "Image for {}".format(self.tour.title)
    

#Fleet Model
class Car(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    image = models.ImageField(upload_to='cars/', null=False, blank=False)
    ban_type = models.CharField(max_length=50, null=False, blank=False)
    lux_type = models.CharField(max_length=50, null=False, blank=False)
    person_count = models.IntegerField(default=0)
    luggage_count = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')
    updated = models.DateTimeField(auto_now=True, verbose_name='Last Updated')

    class Meta:
        ordering = ['-created']
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'

    def __str__(self):
        return self.name

class PriceByWayCount(models.Model):
    car = models.ForeignKey(Car, related_name='prices', on_delete=models.CASCADE)
    way_count = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Car prices by way count'
        verbose_name_plural = 'Cars prices by way count'

    def __str__(self):
        return f"{self.car.name} - {self.way_count} way - ${self.price}"
    

# Contact Model 
class ContactRequest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    website = models.URLField(blank=True, null=True)
    additional_request = models.TextField(blank=True, null=True)
    viewed = models.BooleanField(default=False, verbose_name='Baxdım')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Göndərilmə Tarixi')

    class Meta:
        ordering = ['-created']
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return f"Contact request from {self.name}"
    

# Social media Model
class Social(models.Model):
    PLATFORM_CHOICES = [
        ('facebook', 'Facebook'),
        ('instagram', 'Instagram'),
        ('tiktok', 'TikTok'),
        ('whatsapp', 'WhatsApp'),
        ('wechat', 'WeChat'),
    ]
    
    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES, unique=True)
    link = models.URLField(max_length=200)

    def __str__(self):
        return self.platform

    @staticmethod
    def get_link(platform_name):
        try:
            return Social.objects.get(platform=platform_name).link
        except Social.DoesNotExist:
            return None


# Our Information Model 
class OurInformation(models.Model):
    INFORMATION_CHOICES = [
        ('location', 'Location'),
        ('email', 'Email'),
        ('number', 'Number'),
    ]
    
    type = models.CharField(max_length=255, choices=INFORMATION_CHOICES, unique=True)
    content = models.TextField()

    def __str__(self):
        return self.type


# FAQ Model 
class Faq(models.Model):
    question = models.TextField()
    answer = models.TextField()
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')

    class Meta:
        ordering = ['-created']
        verbose_name = 'Faq'
        verbose_name_plural = 'Faqs'

    def __str__(self):
        return self.question
    

# Updates Request Model
class UpdatesRequest(models.Model):
    email = models.EmailField(unique=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')

    class Meta:
        ordering = ['-created']
        verbose_name = 'UpdateRequest'
        verbose_name_plural = 'UpdatesRequest'

    def __str__(self):
        return self.email
    
# Home Page First Content Model 
class HomeFirstContent(models.Model):
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')
    updated = models.DateTimeField(auto_now=True, verbose_name='Last Updated')
    
    class Meta:
        ordering = ['-created']
        verbose_name = 'Home First Content'
        verbose_name_plural = 'Home First Contents'

    def __str__(self):
        return self.content
    

# FleetForm Model 
class FleetForm(models.Model):
    PICKUP_LOCATION_CHOICES = [
        ('gyd-airport', 'from GYD airport'),
        ('hotel', 'from Hotel'),
    ]
    
    CAR_CLASS_CHOICES = [
        ('economy', 'Economy'),
        ('comfort', 'Comfort'),
        ('business', 'Business'),
        ('premium', 'Premium'),
        ('vip', 'VIP'),
        ('suv', 'SUV'),
        ('van', 'Van'),
        ('minibus', 'Minibus'),
        ('bus', 'Bus'),
    ]
    
    pickup_location = models.CharField(max_length=255, choices=PICKUP_LOCATION_CHOICES)
    dropoff_location = models.CharField(max_length=255)
    date_of_service = models.DateField()
    time_of_service = models.TimeField()
    car_class = models.CharField(max_length=255, choices=CAR_CLASS_CHOICES)
    flight_number = models.CharField(max_length=50, blank=True)
    additional_request = models.TextField(blank=True)
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    viewed = models.BooleanField(default=False, verbose_name='Baxdım')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Göndərilmə Tarixi')

    class Meta:
        ordering = ['-created']
        verbose_name = 'Fleet Form'
        verbose_name_plural = 'Fleet Forms'

    def __str__(self):
        return self.full_name
    

# TourForm Model 
class TourForm(models.Model):
    CAR_CLASS_CHOICES = [
        ('economy', 'Economy'),
        ('comfort', 'Comfort'),
        ('business', 'Business'),
        ('premium', 'Premium'),
        ('vip', 'VIP'),
        ('suv', 'SUV'),
        ('van', 'Van'),
        ('minibus', 'Minibus'),
        ('bus', 'Bus'),
    ]
    
    select_city = models.ManyToManyField(City, related_name='select_city')
    planned_tour_days = models.IntegerField(default=1)
    travel_date = models.DateField()
    car_class = models.CharField(max_length=255, choices=CAR_CLASS_CHOICES)
    additional_request = models.TextField(blank=True)
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    viewed = models.BooleanField(default=False, verbose_name='Baxdım')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Göndərilmə Tarixi')

    class Meta:
        ordering = ['-created']
        verbose_name = 'Tour Form'
        verbose_name_plural = 'Tour Forms'

    def __str__(self):
        return self.full_name
    