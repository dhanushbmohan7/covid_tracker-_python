from django.contrib import admin
from .models import Countries
# Register your models here.
class country(admin.ModelAdmin):
    list_display=('name',)

admin.site.register(Countries,country)    