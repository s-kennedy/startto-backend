from django.contrib import admin
from startto_backend.apps.core.models import Category, Program

# Register your models here.

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'submittable_id'
    ]

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
    ]