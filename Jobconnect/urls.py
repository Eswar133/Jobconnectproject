from django.urls import path
from django.contrib import admin

from carrers.views import (
    LoginView, SignupView,JobForm,LocationFormView,SkillFormView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('my-login/', LoginView.as_view(), name='my-login'),
    path('my-signup/', SignupView.as_view(), name='my-signup'),
    path('job-creation/', JobForm.as_view(), name='job_creation'),
    path('job_location/',LocationFormView.as_view(),name='job_location'),
    path('SkillFormView/',SkillFormView.as_view(),name='skill_form.html')
    

]
