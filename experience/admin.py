from django.contrib import admin
from .models import *
# Register your models here.
class experienceImageAdmin(admin.StackedInline):
    model = experienceImage

class experienceAdmin(admin.ModelAdmin):
    fields = [
        "company_name",
        "position_name",
        "date_started",
        "date",
        "date_ended",
        "position_detail",
    ]

    inlines = [experienceImageAdmin]
    class Meta:
        model = experienceList

admin.site.register(experienceList, experienceAdmin)
