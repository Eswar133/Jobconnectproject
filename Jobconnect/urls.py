from django.urls import path
from django.contrib import admin

from carrers import views
from carrers.views import (
    LoginView, SignupView,JobForm,SkillsPageView,GetSkillsView,StudentJobListView,ApplyJobView,LogoutView,JobsPostedView,JobsAppliedView
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
    path('logout/', LogoutView.as_view(), name='my-logout'),
    path('jobs/my_posted/', JobsPostedView.as_view(), name='my_jobs_posted'),
    path('jobs/applied/', JobsAppliedView.as_view(), name='jobs_applied'),
    
    
]