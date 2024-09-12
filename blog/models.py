from django.db import models
from utils.model.field_utils import get_slug, get_slug_link
from django.urls import reverse
from django.contrib.admin import display

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')
    updated = models.DateTimeField(auto_now=True, verbose_name='Last Updated')

    class Meta:
        ordering = ['-created']
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')
    updated = models.DateTimeField(auto_now=True, verbose_name='Last Updated')

    class Meta:
        ordering = ['-created']
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.TextField()
    slug = models.SlugField(null=True, blank=True, max_length=100, unique=True)
    image = models.ImageField(upload_to='blogs/', null=False, blank=False, verbose_name='Blog Image')
    content = models.TextField()
    viewed = models.IntegerField(default=0, verbose_name='View Count')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=False)
    tags = models.ManyToManyField(Tag)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')
    updated = models.DateTimeField(auto_now=True, verbose_name='Last Updated')

    class Meta:
        ordering = ['-updated']
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_slug(self.title)
        return super().save(*args, **kwargs)
    
    @display(description='Link')
    def slug_link(self):
        return get_slug_link(self.slug, self.get_absolute_url)

    def get_absolute_url(self):
        return reverse("blog:blog-detail", kwargs={"pk": self.pk, "slug": self.slug})

    def get_seo_title(self):
        length = len(self.title)
        if length > 59:
            return self.title[:56] + '...'
        elif length < 9:
            return self.title + ' - Luxtripbaku a company experienced in organizing transfers and tours'
        elif length < 19:
            return self.title + ' - Luxtripbaku experienced company'
        elif length < 29:
            return self.title + ' - Luxtripbaku company'
        elif length < 39:
            return self.title + ' - Luxtripbaku'
        elif length < 49:
            return self.title + ' - Luxtrip'
        else:
            return self.title
