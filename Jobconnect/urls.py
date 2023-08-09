from django.contrib import admin
from django.urls import path
from carrers import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
]
