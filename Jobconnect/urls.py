from django.urls import path
from django.contrib import admin

from carrers.views import (
    LoginView, SignupView,JobForm
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('my-login/', LoginView.as_view(), name='my-login'),
    path('my-signup/', SignupView.as_view(), name='my-signup'),
    path('job-creation/', JobForm.as_view(), name='job_creation'),

]
