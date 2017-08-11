from django.contrib import admin
from .models import Category, Faq


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Faq)
admin.site.register(Category, CategoryAdmin)
