from django import forms
from django.contrib import admin
from django.template.loader import render_to_string
from carrers.models import Skill, Company, Job, JobLocation



class JobLocationAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)




class JobAdmin(admin.ModelAdmin):
    list_display = ['title']
    
admin.site.register(Skill)
admin.site.register(Company)
admin.site.register(Job, JobAdmin)
admin.site.register(JobLocation, JobLocationAdmin)
