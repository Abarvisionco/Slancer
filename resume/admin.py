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

class FieldAdmin(admin.ModelAdmin):
    list_display = ('name', 'best')
    search_fields = ('name',)
    list_filter = ('best',)

class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'level', 'resume')
    list_filter = ('level',)
    search_fields = ('name',)


class ResumeAdmin(admin.ModelAdmin):
    ordering = ('update_date',)
    list_per_page = 100
    list_display = ('user','school','active','update_date')
    search_fields = ('user','school','about')
    list_filter = ('active','update_date','create_time')


admin.site.register(models.Resume, ResumeAdmin)
admin.site.register(models.City, CityAdmin)
admin.site.register(models.State, StateAdmin)
admin.site.register(models.Courses)
admin.site.register(models.WorkExperience)
admin.site.register(models.ExamWorks)
admin.site.register(models.Skills, SkillAdmin)
admin.site.register(models.District, DistrictAdmin)
admin.site.register(models.Field, FieldAdmin)
admin.site.register(models.Language, SkillAdmin)