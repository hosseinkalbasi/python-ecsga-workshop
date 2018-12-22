from django.contrib import admin
from myapp.models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name','university', 'city']


admin.site.register(Student, StudentAdmin)

# before (the simple one)
# admin.site.register(Student)