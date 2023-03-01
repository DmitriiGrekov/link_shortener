from django.contrib import admin
from .models import Link


@admin.register(Link)
class AdminLink(admin.ModelAdmin):
    readonly_fields = ('code',)
