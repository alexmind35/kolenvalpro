from django.contrib import admin

from .models import Hero, Services, Why


@admin.register(Hero)
class AdminHero(admin.ModelAdmin):
    list_display = ["heading_hero", "image_hero"]


@admin.register(Services)
class AdminServices(admin.ModelAdmin):
    list_display = ["name_services"]


@admin.register(Why)
class AdminWhy(admin.ModelAdmin):
    list_display = ["name_why", "text_why"]
