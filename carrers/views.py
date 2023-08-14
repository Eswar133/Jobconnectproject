from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect,HttpResponse,get_object_or_404
from django.utils.decorators import method_decorator
from django.views import View
from .models import JobLocation, Skill,Job
from datetime import datetime
from django.http import JsonResponse



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

class JobForm(View):
    template_name='job_creation.html'

    def get(self, request):
        return render(request, self.template_name)
    
    class JobForm(View):
        template_name = 'job_creation.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        title = request.POST.get('title')
        description = request.POST.get('description')
        role = request.POST.get('role')
        industry_type = request.POST.get('industry_type')
        no_of_openings = request.POST.get('no_of_openings')
        location_name = request.POST.get('location_name')
        location = JobLocation.create_or_get_location(location_name)
        employment_type = request.POST.get('employment_type')
        duration_in_months = request.POST.get('duration_in_months')
        created_on = request.POST.get('created_on')
        valid_until = request.POST.get('valid_until')
        is_active = request.POST.get('is_active')
        salary_visible = request.POST.get('salary_visible')
        min_salary = request.POST.get('min_salary')
        max_salary = request.POST.get('max_salary')
        education_level = request.POST.get('education_level')
        years_of_experience = request.POST.get('years_of_experience')
        company_name = request.POST.get('company_name')
        company, created = Company.objects.get_or_create(company_name='TCS')
        mandatory_skill_names = request.POST.getlist('skills_mandatory')
        optional_skill_names = request.POST.getlist('skills_optional')
        mandatory_skills = [Skill.objects.get_or_create(name=name)[0] for name in mandatory_skill_names]
        optional_skills = [Skill.objects.get_or_create(name=name)[0] for name in optional_skill_names]

        job = Job.objects.create(
            title=title,
            description=description,
            role=role,
            industry_type=industry_type,
            how_many_openings=no_of_openings,
            location=location,
            how_many_applied=0,
            employment_type=employment_type,
            intern_months=duration_in_months,
            created_on=created_on,
            validity_until=valid_until,
            is_active=is_active,
            salary_available=salary_visible,
            min_salary=min_salary,
            max_salary=max_salary,
            education_level=education_level,
            years_of_experience=years_of_experience,
            company_info=company,
        )
        job.skills_mandatory.set(mandatory_skills)
        job.skills_optional.set(optional_skills)

        return redirect('job_list')
