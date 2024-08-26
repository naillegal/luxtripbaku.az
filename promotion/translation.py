from modeltranslation.translator import register, TranslationOptions
from .models import City, Tour, TourImage, Car, Faq, HomeFirstContent, Whoweare


@register(City)
class CityTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Tour)
class TourTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(TourImage)
class TourImageTranslationOptions(TranslationOptions):
    fields = ('caption',)


@register(Car)
class CarTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Faq)
class FaqTranslationOptions(TranslationOptions):
    fields = ('question', 'answer',)


@register(HomeFirstContent)
class HomeFirstContentTranslationOptions(TranslationOptions):
    fields = ('content',)


@register(Whoweare)
class WhoweareTranslationOptions(TranslationOptions):
    fields = ('head_title', 'content',)
