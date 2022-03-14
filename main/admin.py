from django.contrib import admin
from django.db import models

from .models import Project, ProjectCategory, ProjectSeries
from tinymce.widgets import TinyMCE

# Register your models here.


class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Title/date", {"fields": ["project_title", "project_published"]}),
        ("URL", {"fields": ["project_slug"]}),
        ("Series", {"fields": ["project_series"]}),
        ("Content", {"fields": ["project_content"]}),
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }

admin.site.register(ProjectSeries)
admin.site.register(ProjectCategory)
admin.site.register(Project, ProjectAdmin)
