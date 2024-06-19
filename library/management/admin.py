from django.contrib import admin
from django.contrib.admin import register, ModelAdmin
from .models import *

@register(Author)
class  AuthorAdmin(ModelAdmin):
    list_display = ['name']


@register(Book)
class  BookAdmin(ModelAdmin):
    list_display = ['title', 'count']


@register(Member)
class  MemberAdmin(ModelAdmin):
    list_display = ['name']


@register(Reservation)
class  ReservationAdmin(ModelAdmin):
    list_display = ['book', 'member', 'status']
    search_fields = ['book__title', 'member__name']

# Register your models here.
