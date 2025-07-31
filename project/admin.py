from django.contrib import admin
from .models import Project

class EmployeeAdmin(admin.ModelAdmin):  
	readonly_fields = ('created',)

admin.site.register(Project, EmployeeAdmin)