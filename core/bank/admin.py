from django.contrib import admin

from bank.models import Customer

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'balance')

admin.site.register(Customer, CustomerAdmin)