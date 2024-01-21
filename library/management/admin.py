from django.contrib import admin
from django.contrib.admin import register, ModelAdmin
from .models import *

# @register(Author)
class  AuthorAdmin(ModelAdmin):
    list_display = ['name']

# Register your models here.
