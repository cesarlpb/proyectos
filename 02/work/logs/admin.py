from django.contrib import admin
from logs.models import WorkLog

class WorkLogAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_time', 'end_time', 'duration')
    search_fields = ('title', 'description')
    list_filter = ('start_time', 'end_time')
    ordering = ('start_time',)
    readonly_fields = ('duration',)

    def save_model(self, request, obj, form, change):
        # Calcula la duración automáticamente al guardar el objeto
        obj.duration = obj.end_time - obj.start_time
        super().save_model(request, obj, form, change)

admin.site.register(WorkLog, WorkLogAdmin)
