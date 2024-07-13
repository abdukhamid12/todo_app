from django.contrib import admin
from task.models import Task

# Register your models here.

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("id", "title_display", "description_display", "created_at", "updated_at")

    def title_display(self, obj):
        return f"{obj.title[:10]}..." if len(obj.title) > 10 else obj.title

    def description_display(self, obj):
        return f"{obj.description[0:40]}..." if len(obj.description) > 40 else obj.description