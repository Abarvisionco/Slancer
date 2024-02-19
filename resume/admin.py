from django.contrib import admin
from resume import models

# make good view for admin panel
class StateAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class CityAdmin(admin.ModelAdmin):
    list_display = ('name','state')
    search_fields = ('state','name')

class DistrictAdmin(admin.ModelAdmin):
    list_display = ('name','city')
    search_fields = ('name',)

class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name', 'district','phone_number')
    search_fields = ('name','about')

class FieldAdmin(admin.ModelAdmin):
    list_display = ('name', 'best')
    search_fields = ('name',)
    list_filter = ('best',)

class ResumeAdmin(admin.ModelAdmin):
    list_display = ('user','school','email','active')
    search_fields = ('user','school','about','email')
    list_filter = ('active',)


admin.site.register(models.School, SchoolAdmin)
admin.site.register(models.Resume, ResumeAdmin)
admin.site.register(models.City, CityAdmin)
admin.site.register(models.State, StateAdmin)
admin.site.register(models.Courses)
admin.site.register(models.WorkExperience)
admin.site.register(models.ExamWorks)
admin.site.register(models.Skills)
admin.site.register(models.District, DistrictAdmin)
admin.site.register(models.Field, FieldAdmin)
