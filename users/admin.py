from django.contrib import admin
from users import models



'''
    Register User Model on admin panel django
'''

class UserAdmin(admin.ModelAdmin):
    list_filter = ['is_superuser','is_admin']
    search_fields = ['mobile','first_name',"last_name"]
    list_display = ['mobile','first_name','last_name','is_superuser','is_admin']



admin.site.register(models.User,UserAdmin)