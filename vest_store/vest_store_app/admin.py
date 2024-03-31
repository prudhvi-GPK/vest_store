# admin.py
from django.contrib import admin
from .models import Vest

@admin.register(Vest)
class VestAdmin(admin.ModelAdmin):
    list_display = ('size', 'price', 'stock')
    list_editable = ('price', 'stock')
    list_filter = ('size',)
