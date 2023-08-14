from django.urls import path
from django.contrib import admin

from carrers.views import (
    LoginView, SignupView, JobCreateView,MyHome
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('my-login/', LoginView.as_view(), name='my-login'),
    path('my-signup/', SignupView.as_view(), name='my-signup'),
    path('job-creation/', JobCreateView.as_view(), name='job_creation'),
    path('my-home/',MyHome.as_view(),name="my-home"),
    

]
