from django.contrib import admin
from django.utils.html import format_html
from .models import City, Tour, TourImage, Car, ContactRequest, Social, OurInformation, Faq, UpdatesRequest, HomeFirstContent,FleetForm, TourForm,PriceByWayCount,Whoweare
from django.contrib.admin import DateFieldListFilter
from modeltranslation.admin import TranslationAdmin


# CustomTranslationAdmin 
class CustomTranslationAdmin(TranslationAdmin):
    group_fieldsets = True

    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

# Tour Admin
class TourImageInline(admin.TabularInline):
    model = TourImage
    extra = 1
    fields = ('image', 'caption', 'image_thumbnail')

    readonly_fields = ('image_thumbnail',)

    def image_thumbnail(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 75px; height: 50px;" />', obj.image.url)
        return "-"
    image_thumbnail.short_description = 'Image'


@admin.register(City)
class CityAdmin(CustomTranslationAdmin):
    list_display = ('name', 'created', 'updated')
    list_filter = (
        ('created', DateFieldListFilter),
        ('updated', DateFieldListFilter),
    )

@admin.register(Tour)
class TourAdmin(CustomTranslationAdmin):
    list_display = ('title', 'city', 'created', 'updated')
    list_filter = (
        'city',
        ('created', DateFieldListFilter),
        ('updated', DateFieldListFilter),
    )
    inlines = [TourImageInline]


@admin.register(TourImage)
class TourImageAdmin(CustomTranslationAdmin):
    list_display = ('tour', 'caption', 'created', 'updated', 'image_thumbnail')
    list_filter = (
        'tour',
        ('created', DateFieldListFilter),
        ('updated', DateFieldListFilter),
    )

    readonly_fields = ('image_thumbnail',)

    def image_thumbnail(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 75px; height: 50px;" />', obj.image.url)
        return "-"
    image_thumbnail.short_description = 'Image'


# Fleet Admin
@admin.register(Car)
class CarAdmin(CustomTranslationAdmin):
    list_display = ('thumbnail', 'name', 'ban_type', 'lux_type', 'person_count', 'luggage_count', 'created', 'updated')
    list_filter = ('ban_type', 'lux_type', 'created', 'updated')
    search_fields = ('name', 'ban_type', 'lux_type')
    ordering = ('-created',)
    readonly_fields = ('created', 'updated', 'thumbnail')

    fieldsets = (
        (None, {
            'fields': ('name', 'image', 'thumbnail', 'ban_type', 'lux_type', 'person_count', 'luggage_count')
        }),
        ('Timestamps', {
            'fields': ('created', 'updated')
        }),
    )

    def thumbnail(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="75px" height="50px" />', obj.image.url)
        return ""
    thumbnail.short_description = 'Image Preview'

@admin.register(PriceByWayCount)
class PriceByWayCountAdmin(admin.ModelAdmin):
    list_display = ('car', 'way_count', 'price')
    list_filter = ('car', 'way_count')
    search_fields = ('car__name', 'way_count')
    ordering = ('car', 'way_count')

    fieldsets = (
        (None, {
            'fields': ('car', 'way_count', 'price')
        }),
    )


# Contact Admin
@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'website', 'viewed', 'created')
    list_filter = ('created',)
    search_fields = ('name', 'email', 'phone', 'viewed')
    readonly_fields = ('created',)
    ordering = ('-created',)


# Social Admin
@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    list_display = ('platform', 'link')
    search_fields = ('platform',)


# OurInformation Admin
@admin.register(OurInformation)
class OurInformationAdmin(admin.ModelAdmin):
    list_display = ('type', 'content')
    search_fields = ('type',)


# FAQ Admin
@admin.register(Faq)
class FaqAdmin(CustomTranslationAdmin):
    list_display = ('question',)
    readonly_fields = ('created',)
    list_filter = (
        ('created', DateFieldListFilter),
    )


# UpdatesRequest Admin
@admin.register(UpdatesRequest)
class UpdatesRequest(admin.ModelAdmin):
    readonly_fields = ('created',)
    list_filter = (
        ('created', DateFieldListFilter),
    )


# HomeFirstContent Admin
@admin.register(HomeFirstContent)
class HomeFirstContent(CustomTranslationAdmin):
    readonly_fields = ('created',)
    list_filter = (
        ('created', DateFieldListFilter),
    )

# FleetForm Admin 
@admin.register(FleetForm)
class FleetFormAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'created', 'viewed')
    list_filter = ('viewed', 'date_of_service', 'car_class')
    search_fields = ('full_name', 'email', 'phone', 'dropoff_location', 'flight_number')
    readonly_fields = ('created',)
    actions = ['mark_as_viewed']

    def mark_as_viewed(self, request, queryset):
        queryset.update(viewed=True)
    mark_as_viewed.short_description = "Mark selected forms as viewed"


# TourForm Admin 
@admin.register(TourForm)
class TourFormAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'created', 'viewed')
    list_filter = ('viewed', 'travel_date', 'car_class')
    search_fields = ('full_name', 'email', 'phone')
    readonly_fields = ('created',)
    actions = ['mark_as_viewed']
    
    def mark_as_viewed(self, request, queryset):
        queryset.update(viewed=True)
    mark_as_viewed.short_description = "Mark selected tour forms as viewed"


# Who we are admin
@admin.register(Whoweare)
class WhoweareAdmin(CustomTranslationAdmin):
    list_display = ('head_title',)
    
    def thumbnail(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="120;" height="80;" />', obj.image.url)
        return ""
    thumbnail.short_description = 'Current Image'

    readonly_fields = ('thumbnail',)

    fieldsets = (
        (None, {
            'fields': ('thumbnail', 'image', 'head_title', 'content',)
        }),
    )