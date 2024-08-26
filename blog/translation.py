from modeltranslation.translator import register, TranslationOptions
from .models import Blog, Category, Tag


@register(Blog)
class BlogTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Tag)
class TagTranslationOptions(TranslationOptions):
    fields = ('title',)
