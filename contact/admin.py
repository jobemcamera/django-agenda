from django.contrib import admin
from contact import models


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name', 'phone', 'email', 'show',
    list_filter = 'created_date',
    ordering = 'id',
    search_fields = 'id', 'first_name', 'last_name', 'phone', 'email',
    list_per_page = 10
    list_max_show_all = 100

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'id', 'name',
    list_filter = 'name',
    ordering = 'id',
    search_fields = 'id', 'name',
    list_per_page = 10
    list_max_show_all = 100
