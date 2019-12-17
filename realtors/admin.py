from django.contrib import admin

from .models import Realtor

class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'neme', 'email', 'hire_date')
    list_display_links = ('id', 'neme')
    search_fields = ('neme',)
    list_per_page = 25

admin.site.register(Realtor, RealtorAdmin)
