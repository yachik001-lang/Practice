from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "verified", "created_at")
    list_filter = ("verified", "created_at")
    search_fields = ("full_name", "email", "text")
    list_editable = ("verified",)