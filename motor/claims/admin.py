from django.contrib import admin
from .models import UserInformation, Vehicle, Loss, Document

class VehicleInline(admin.TabularInline):
    classes = ['collapse']
    model = Vehicle
    extra = 1

    # list_display = ("vehicle_year", "vehicle_model", "vehicle_num")

class LossInline(admin.StackedInline):
    classes = ['collapse']
    verbose_name = "Loss"
    model = Loss
    extra = 1

class DocumentInline(admin.StackedInline):
    classes = ['collapse']
    verbose_name = "Document"
    model = Document
    extra = 1

@admin.register(UserInformation)
class UserInformationsAdmin(admin.ModelAdmin):
# 'classes': ['collapse']

    list_display = ("name", "email", "mobile", "status")
    fieldsets = [
        ("DRIVER DETAILS", {'fields': ['name']}),
        (None, {'fields': ['email']}),
        (None, {'fields': ['mobile']}),
        (None, {'fields': ['status']}),
    ]
    inlines = [
        VehicleInline,
        LossInline,
        DocumentInline
    ]
