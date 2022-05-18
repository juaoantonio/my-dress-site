from django.contrib import admin
from .models import Vestido


@admin.register(Vestido)
class VestidoAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "created_at", "updated_at")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name",)
    list_filter = ("created_at",)
    ordering = ("-created_at",)
