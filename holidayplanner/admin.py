from holidayplanner.models import Employee
from django.contrib import admin

class EmployeeAdmin(admin.ModelAdmin):
	fields = ['empId','startDate']

admin.site.register(Employee,EmployeeAdmin)
