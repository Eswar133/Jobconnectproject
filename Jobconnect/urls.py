from django.urls import path
from django.contrib import admin


from carrers.views import (
    LoginView, SignupView,JobForm,LocationListView,SkillListView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('my-login/', LoginView.as_view(), name='my-login'),
    path('my-signup/', SignupView.as_view(), name='my-signup'),
    path('job-creation/', JobForm.as_view(), name='job_creation'),
    path('locations/',LocationListView.as_view(),name='location-list'),
    path('skills/',SkillListView.as_view(),name='skill-list'),
]
