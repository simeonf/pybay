from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin

from .models import Job

class JobAdmin(OrderedModelAdmin):
    prepopulated_fields = {"url": ("title",)}
    list_display = ('title', 'details', 'display', 'level', 'location', 'move_up_down_links')
    list_filter = ('display',)

admin.site.register(Job, JobAdmin)
