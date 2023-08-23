from django.urls import path
from django.contrib import admin

from carrers import views
from carrers.views import (
    LoginView, SignupView,JobForm,SkillsPageView,GetSkillsView,StudentJobListView,ApplyJobView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('my-login/', LoginView.as_view(), name='my-login'),
    path('my-signup/', SignupView.as_view(), name='my-signup'),
    path('job-creation/', JobForm.as_view(), name='job_creation'),
    path('skills_page/', SkillsPageView.as_view(), name='skills_page'),
    path('get_skills/', GetSkillsView.as_view(), name='get_skills'),
    path('student_jobs/', StudentJobListView.as_view(), name='student_jobs'),
    path('apply_job/',ApplyJobView.as_view(), name='apply_job'),
    
]