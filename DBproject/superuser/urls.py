from django.urls import path
from . import views

urlpatterns = [
    path('', views.adminCode),
    path('hire_info/',views.hire_info),
    path('company_info/', views.company_info),
]