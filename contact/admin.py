from django.contrib import admin
from contact import models

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'created_date')
    search_fields = ('first_name', 'last_name', 'email', 'phone')
    list_filter = ('created_date',)
    date_hierarchy = 'created_date'
    ordering = ('-created_date',)
    list_per_page = 10

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    