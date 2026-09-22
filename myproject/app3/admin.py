from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'created_at')
    search_fields = ('name', 'email', 'phone', 'notes')
    list_filter = ('created_at',)
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
