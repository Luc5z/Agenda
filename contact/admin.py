from django.contrib import admin
from contact import models

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    search_fields = ('first_name', 'last_name', 'email', 'phone')
    list_filter = ('created_date',)
    date_hierarchy = 'created_date'
    ordering = ('-created_date',)