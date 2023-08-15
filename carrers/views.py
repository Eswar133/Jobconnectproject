from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect,HttpResponse,get_object_or_404
from django.utils.decorators import method_decorator
from django.views import View
from .models import JobLocation, Skill,Job,Company
from datetime import datetime
from django.http import JsonResponse
from django.contrib import messages

class SignupView(View):
    template_name = 'my-signup.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return HttpResponse("Your password and confirm password are not the same!!")
        else:
            try:
                existing_user = User.objects.get(username=uname)
                return HttpResponse("Username already exists. Please choose a different username.")
            except User.DoesNotExist:
                my_user = User.objects.create_user(username=uname, email=email, password=pass1)
                my_user.save()
                return redirect('my-login')

class LoginView(View):
    template_name = 'my-login.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('job_creation')
        else:
            return HttpResponse("Username or Password is incorrect!!!")

def LogoutPage(request):
    logout(request)
    return redirect('my-login')


class LocationFormView(View):
    template_name = 'job_location.html'  # Create a template named location_form.html

    @method_decorator(login_required)
    def get(self, request):
        return render(request, self.template_name)

    @method_decorator(login_required)
    def post(self, request):
        location_name = request.POST.get('location_name')
        location, created = JobLocation.objects.get_or_create(name=location_name)
        messages.success(request, f'Location "{location_name}" added successfully')
        return redirect('job_creation')


class SkillFormView(View):
    template_name = 'skill_form.html'  # Create a template named skill_form.html

    @method_decorator(login_required)
    def get(self, request):
        return render(request, self.template_name)

    @method_decorator(login_required)
    def post(self, request):
        mandatory_skill_name = request.POST.get('skills_mandatory')
        optional_skill_name = request.POST.get('skills_optional')
        skill, created = Skill.objects.get_or_create(name=mandatory_skill_name)
        skill, created = Skill.objects.get_or_create(name=optional_skill_name)
        messages.success(request, f'Skill "{mandatory_skill_name} " added successfully')
        messages.success(request, f'Skill "{optional_skill_name} " added successfully')
        return redirect('job_creation')


class JobForm(View):
    template_name = 'job_creation.html'

    @method_decorator(login_required)
    def get(self, request):
        skills_mandatory = Skill.objects.all()
        skills_optional = Skill.objects.all()
        job_locations = JobLocation.objects.all()
        return render(request, self.template_name, {
            'skills_mandatory': skills_mandatory,
            'skills_optional': skills_optional,
            'job_locations': job_locations,
        })

    @method_decorator(login_required)
    def post(self, request):
        title = request.POST.get('title')
        description = request.POST.get('description')
        role = request.POST.get('role')
        industry_type = request.POST.get('industry_type')
        no_of_openings = int(request.POST.get('no_of_openings', 0))
        location_id = int(request.POST.get('location_name'))
        location=get_object_or_404(JobLocation,id=location_id)
        employment_type = request.POST.get('employment_type')
        duration_in_months = int(request.POST.get('duration_in_months', 0))
        created_on = datetime.now()
        valid_until = datetime.strptime(request.POST.get('valid_until'), '%Y-%m-%d')
        is_active = bool(request.POST.get('is_active', False))
        salary_visible = bool(request.POST.get('salary_visible', False))
        min_salary = int(request.POST.get('min_salary', 0))
        max_salary = int(request.POST.get('max_salary', 0))
        education_level = request.POST.get('education_level')
        years_of_experience = int(request.POST.get('years_of_experience', 0))
        company_name = request.POST.get('company_name')
        company, created = Company.objects.get_or_create(company_name=company_name)
        
        # Handle mandatory skills
        mandatory_skill_ids = request.POST.getlist('skills_mandatory')
        mandatory_skills = Skill.objects.filter(pk__in=mandatory_skill_ids)

        # Handle optional skills
        optional_skill_ids = request.POST.getlist('skills_optional')
        optional_skills = Skill.objects.filter(pk__in=optional_skill_ids)

        # Create job instance and save
        job = Job.objects.create(
            title=title,
            description=description,
            role=role,
            industry_type=industry_type,
            location=location,
            no_of_openings=no_of_openings,
            employment_type=employment_type,
            duration_in_months=duration_in_months,
            created_on=created_on,
            valid_until=valid_until,
            is_active=is_active,
            salary_visible=salary_visible,
            min_salary=min_salary,
            max_salary=max_salary,
            education_level=education_level,
            years_of_experience=years_of_experience,
            company_info=company,
        )

        # Add mandatory and optional skills to the job instance
        job.skills_mandatory.set(mandatory_skills)
        job.skills_optional.set(optional_skills)
        job.save()

        messages.success(request, 'Job created successfully')
        return redirect('job_creation')

