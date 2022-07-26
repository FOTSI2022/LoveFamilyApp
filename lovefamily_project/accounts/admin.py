from django.contrib import admin
from .models import Person

# Register your models here.
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display=('id', 'gender', 'father', 'mother', 'phone_number', 'email', 'occupation', 'birth_country', 'birth_region', 'history', 'personallyregister', 'user')
    list_per_page=20
