from django.db import models

    
class Skill(models.Model):
    name=models.CharField(max_length=20)
    
    def __str__(self):
        return self.name

class Company(models.Model):
    company_name = models.CharField(max_length=255)
    address = models.TextField()
    website = models.URLField()

class JobLocation(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

    def __str__(self):
        return self.company_name
class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    role = models.CharField(max_length=255)
    industry_type = models.CharField(max_length=255)
    how_many_openings = models.IntegerField()
    location = models.ForeignKey('JobLocation', on_delete=models.CASCADE)
    no_of_openings = models.IntegerField()
    employment_type = models.CharField(max_length=50)
    duration_in_months = models.IntegerField(null=True, blank=True)
    created_on = models.DateField()
    valid_until = models.DateField()
    is_active = models.BooleanField()
    salary_visible = models.BooleanField(null=True)
    min_salary = models.PositiveSmallIntegerField(null=True, blank=True)
    max_salary = models.PositiveSmallIntegerField(null=True, blank=True)
    education_level = models.CharField(max_length=255)
    years_of_experience = models.PositiveSmallIntegerField()
    skills_mandatory = models.ManyToManyField(Skill, related_name='jobs_mandatory')
    skills_optional = models.ManyToManyField(Skill, related_name='jobs_optional')
    company_info = models.ForeignKey(Company, on_delete=models.CASCADE)
    skills_mandatory = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name='jobs_mandatory')
    skills_optional = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name='jobs_optional')


    def __str__(self):
        return self.title
    def create_or_get_location(cls, location_name):
        location, created = JobLocation.objects.get_or_create(name=location_name)
        return location
    
    
