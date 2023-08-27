from django.db import models
from django.contrib.auth.models import User

    
class Skill(models.Model):
    name=models.CharField(max_length=20)
    
    def __str__(self):
        return self.name

class Company(models.Model):
    company_name = models.CharField(max_length=255)
    address = models.TextField(null=True)
    website = models.URLField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)  # Example default value

    def __str__(self):
        return self.company_name

        

class JobLocation(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Job(models.Model):
    EMPLOYMENT_TYPES=[
        ('full_time','Full Time'),
        ('part_time','Part Time'),
        ('contract','Contract'),
    ]
    title = models.CharField(max_length=255)
    description = models.TextField()
    role = models.CharField(max_length=255)
    industry_type = models.CharField(max_length=255)
    location = models.ForeignKey('JobLocation', on_delete=models.CASCADE)
    no_of_openings = models.PositiveSmallIntegerField()
    employment_type = models.CharField(max_length=50,choices=EMPLOYMENT_TYPES)
    duration_in_months = models.PositiveSmallIntegerField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    valid_until = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    salary_visible = models.BooleanField(default=False)
    min_salary = models.PositiveSmallIntegerField(null=True, blank=True)
    max_salary = models.PositiveSmallIntegerField(null=True, blank=True)
    education_level = models.CharField(max_length=255)
    years_of_experience = models.PositiveSmallIntegerField()
    skills_mandatory = models.ManyToManyField(Skill, related_name='mandatory_jobs')
    skills_optional = models.ManyToManyField(Skill, related_name='optional_jobs')
    company_info = models.ForeignKey(Company, on_delete=models.CASCADE,default=1)
    students_applied=models.ManyToManyField(User,related_name='applied_jobs',blank=True)

    def __str__(self):
        return self.title
    
    
    def is_applied_by_student(self, student):
        return student in self.students_applied.all()
    
    @classmethod
    def create_or_get_location(cls, location_name):
        location, created = JobLocation.objects.get_or_create(name=location_name)
        return location
    
    
