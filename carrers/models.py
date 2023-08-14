from django.db import models
from datetime import datetime



class JobLocation(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Skill(models.Model):
    name=models.CharField(max_length=20)
    
    def __str__(self):
        return self.name

class Company(models.Model):
    company_name = models.CharField(max_length=255)
    address = models.TextField()
    website = models.URLField(max_length=200)

    def __str__(self):
        return self.company_name
    
    
class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    role = models.CharField(max_length=255)
    industry_type = models.CharField(max_length=255)
    location=models.CharField(max_length=20)
    number_of_openings = models.PositiveSmallIntegerField()
    
    EMPLOYMENT_TYPE_CHOICES=[
        ('full_time','Full-Time'),
        ('part_time', 'Part-Time'),
        ('work_from_home', 'Work from Home'),
    ]
    employment_type=models.CharField(max_length=50,choices=EMPLOYMENT_TYPE_CHOICES)
    duration_of_employment_months = models.PositiveIntegerField(null=True, blank=True)
    open_until=models.DateTimeField()
    is_active = models.BooleanField()
    salary_visible = models.BooleanField()
    min_salary = models.PositiveSmallIntegerField(null=True, blank=True)
    max_salary = models.PositiveSmallIntegerField(null=True, blank=True)
    EDUCATION_LEVEL_CHOICES = [
        ('btech', 'B.Tech'),
        ('mtech', 'M.Tech'),
        ('mba', 'MBA'),
        ('ms', 'MS'),
        
    ]
    education_level = models.CharField(max_length=255,choices=EDUCATION_LEVEL_CHOICES)#rewrite usingchoices
    years_of_experience = models.PositiveSmallIntegerField()
    skills_mandatory = models.ManyToManyField(Skill, related_name='mandatory_skill_jobs')
    skills_optional = models.ManyToManyField(Skill, related_name='optional_skills_jobs',blank=True)
    created_on=models.DateTimeField(default=datetime.now,blank=True)
    
    

    def __str__(self):
        return self.title
    
    
