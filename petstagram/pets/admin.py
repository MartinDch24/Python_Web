from django.contrib import admin

from petstagram.pets.models import Pets


@admin.register(Pets)
class PetsAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
