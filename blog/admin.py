from django.contrib import admin
from .models import Blog, Category, Tag
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


@admin.register(Blog)
class BlogAdmin(CustomTranslationAdmin):
    list_display = ('title', 'category', 'viewed', 'created', 'updated')
    search_fields = ('title', 'content')
    list_filter = ('category', 'tags', 'created', 'updated',)
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('slug_link', 'viewed')


@admin.register(Category)
class CategoryAdmin(CustomTranslationAdmin):
    list_display = ('title', 'created', 'updated')
    search_fields = ('title',)
    prepopulated_fields = {'title': ('title',)}


@admin.register(Tag)
class TagAdmin(CustomTranslationAdmin):
    list_display = ('title', 'created', 'updated')
    search_fields = ('title',)
