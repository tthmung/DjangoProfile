from django.contrib import admin
from .models import *

# Register your models here.
class projectImaginAdmin(admin.StackedInline):
    model = ProjectImage


class projectAdmin(admin.ModelAdmin):
    fields = ["project_name", "project_detail"]

    inlines = [projectImaginAdmin]

    class Meta:
        model = ProjectList


admin.site.register(ProjectList, projectAdmin)

