from django.contrib import admin
from .models import Blog, Category, Tag

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'viewed', 'created', 'updated')
    search_fields = ('title', 'content')
    list_filter = ('category', 'tags', 'created', 'updated',)
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('slug_link', 'viewed')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'updated')
    search_fields = ('title',)
    prepopulated_fields = {'title': ('title',)}

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'updated')
    search_fields = ('title',)
