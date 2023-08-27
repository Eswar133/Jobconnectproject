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
from django.views.generic import TemplateView,ListView
from django.utils import timezone
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin


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
            role = request.POST.get('role')
            if role == 'candidate':
                return redirect('student_jobs')  # Redirect to student jobs page
            elif role == 'hr':
                return redirect('job_creation')  # Redirect to job creation page
        else:
            return HttpResponse("Username or Password is incorrect!!!")
        
        
class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('my-login')


class JobForm(View):
    template_name = 'carrers/job_creation.html'

    @method_decorator(login_required)
    def get(self, request):
        is_hr = request.user.groups.filter(name='HR').exists()
        skills_mandatory = Skill.objects.all()
        skills_optional = Skill.objects.all()
        job_locations = JobLocation.objects.all()
        companies = Company.objects.filter(user=request.user)
        if companies.exists():
            company = companies.first()  # Choose the first Company object
        else:
            company = None  # No Company object found

        return render(request, self.template_name, {
            'skills_mandatory': skills_mandatory,
            'skills_optional': skills_optional,
            'job_locations': job_locations,
            'is_hr': is_hr,
            'company': company,
        })

    @method_decorator(login_required)
    def post(self, request):
        title = request.POST.get('title')
        description = request.POST.get('description')
        role = request.POST.get('role')
        industry_type = request.POST.get('industry_type')
        no_of_openings = int(request.POST.get('no_of_openings', 0))
        location_name = request.POST.get('location_name')
        location = self.create_or_get_location(location_name)

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
        address = request.POST.get('address')
        website = request.POST.get('website')
        company, created = Company.objects.get_or_create(user=request.user)
        company.company_name = company_name
        company.address = address
        company.website = website
        company.save()
        mandatory_skill_names = request.POST.get('skills_mandatory').split(',')
        mandatory_skills = []

        for skill_name in mandatory_skill_names:
            skill, created = Skill.objects.get_or_create(name=skill_name.strip())
            mandatory_skills.append(skill)

        optional_skill_names = request.POST.get('skills_optional').split(',')
        optional_skills = []

        for skill_name in optional_skill_names:
            skill, created = Skill.objects.get_or_create(name=skill_name.strip())
            optional_skills.append(skill)
        
        
            
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
        job.skills_mandatory.set(mandatory_skills)  # Set the mandatory skill IDs
        job.skills_optional.set(optional_skills)    # Set the optional skill IDs
        job.save()
        response_data = {'message': 'Job created successfully'}
        return JsonResponse(response_data)

    def create_or_get_location(self, location_name):
        location, created = JobLocation.objects.get_or_create(name=location_name)
        return location





    
class GetSkillsView(View):
    def get(self, request, *args, **kwargs):
        skills = Skill.objects.all().values_list('name', flat=True)
        return JsonResponse({'skills': list(skills)})
    
    
class SkillsPageView(TemplateView):
    template_name="carrers/skills_page.html"

class StudentJobListView(ListView):
    model = Job
    template_name = 'carrers/student_jobs.html'
    context_object_name = 'job_listings'
    paginate_by=10
    
    def get_queryset(self):
        queryset=super().get_queryset()
        
        location = self.request.GET.get('location')
        skills = self.request.GET.get('skills')
        experience = self.request.GET.get('experience')
        min_salary = self.request.GET.get('min_salary')
        max_salary = self.request.GET.get('max_salary')
        role=self.request.GET.get('role')
        created_on = self.request.GET.get('created_on')
        valid_until_str = self.request.GET.get('valid_until')
        company_name = self.request.GET.get('company_name')
        duration_in_months = self.request.GET.get('duration_in_months')
        
        
        
        if location:
            queryset = queryset.filter(location__name=location)

        if skills:
            queryset = queryset.filter(Q(title__icontains=skills) | Q(description__icontains=skills))

        if experience:
            queryset = queryset.filter(years_of_experience__gte=experience)

        if min_salary:
            queryset = queryset.filter(min_salary__gte=min_salary)
        
        if max_salary:
            queryset = queryset.filter(max_salary__lte=max_salary)
        
        if role:
            queryset=queryset.filter(role=role)
            
        if created_on:
            created_on = timezone.make_aware(datetime.strptime(created_on, '%Y-%m-%d'))
            queryset = queryset.filter(created_on__date=created_on.date())

        if valid_until_str:
            valid_until = timezone.make_aware(datetime.strptime(valid_until_str, '%Y-%m-%d'))
            queryset = queryset.filter(valid_until__gte=valid_until)

        if company_name:
            queryset = queryset.filter(company_info__company_name__icontains=company_name)

        if duration_in_months:
            queryset = queryset.filter(duration_in_months__gte=duration_in_months)

        
        if created_on :
            created_on=timezone.make_aware(datetime.strptime(created_on, '%Y-%m-%d'))
            queryset = queryset.filter(created_on__date=created_on.date())

        if valid_until_str:
            valid_until = datetime.strptime(valid_until_str, '%Y-%m-%d')
            queryset = queryset.filter(valid_until__gte=valid_until)
        
        if company_name:
            queryset = queryset.filter(company_info__company_name__icontains=company_name)

        if duration_in_months:
            queryset = queryset.filter(duration_in_months__gte=duration_in_months)

        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['username'] = self.request.user.username if self.request.user.is_authenticated else None

        
        
        jobs = self.get_queryset()  # Get the filtered queryset
        paginator = Paginator(jobs, self.paginate_by)  # Create a Paginator instance
        page_number = self.request.GET.get('page')  # Get the page number from the request
        page_obj = paginator.get_page(page_number)  # Get the page object

        context['page_obj'] = page_obj  # Add the page object to the context

        return context
    
class ApplyJobView(View):
    def post(self, request, *args, **kwargs):
        job_id = request.POST.get('job_id')
        student = request.user
        job = Job.objects.get(pk=job_id)

        if not job.is_applied_by_student(student):
            job.students_applied.add(student)
            messages.success(request, 'You have successfully applied for this job.')
        else:
            messages.warning(request, 'You have already applied for this job.')
        
        return redirect('student_jobs') 
    
    
class JobsAppliedView(LoginRequiredMixin, ListView):
    model = Job
    template_name = 'carrers/jobs_applied.html'
    context_object_name = 'job_listings'
    paginate_by = 10

    def get_queryset(self):
        user = self.request.user
        return Job.objects.filter(students_applied=user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.user.username if self.request.user.is_authenticated else None
        return context




class JobsPostedView(LoginRequiredMixin, ListView):
    model = Job
    template_name = 'carrers/my_jobs_posted.html'  
    context_object_name = 'job_listings'
    paginate_by = 10

    def get_queryset(self):
        user = self.request.user
        return Job.objects.filter(company_info__user=user)  # Filter jobs posted by the logged-in user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.user.username if self.request.user.is_authenticated else None
        return context

