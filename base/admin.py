from django.contrib import admin

# Register your models here.

from .models import Groceries

class GroceriesAdmin(admin.ModelAdmin):
    search_fields=['name']
    list_display = ["name", "price"]
    list_filter = ["name", "price"]

admin.site.register(Groceries,GroceriesAdmin)
