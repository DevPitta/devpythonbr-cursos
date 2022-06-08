from django.contrib import admin
from products.models import Plan, Formation, Course


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ['title', 'subtitle', 'created', 'updated']
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Formation)
class FormationAdmin(admin.ModelAdmin):
    list_display = ['title', 'subtitle', 'created', 'updated']
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'subtitle', 'created', 'updated']
    prepopulated_fields = {"slug": ("title",)}
