from django.db import models

    
class Skill(models.Model):
    name=models.CharField(max_length=20)
    
    def __str__(self):
        return self.name

class Company(models.Model):
    company_name = models.CharField(max_length=255)
    address = models.TextField(null=True)
    website = models.URLField(null=True)
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
    skills_mandatory = models.ManyToManyField(Skill, related_name='jobs_mandatory')
    skills_optional = models.ManyToManyField(Skill, related_name='jobs_optional')
    company_info = models.ForeignKey(Company, on_delete=models.CASCADE,default=1)
    

    def __str__(self):
        return self.title
    @classmethod
    def create_or_get_location(cls, location_name):
        location, created = JobLocation.objects.get_or_create(name=location_name)
        return location
    
    
