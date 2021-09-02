from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup),
    path('login/', views.login),
    path('user_main/', views.user_main),
    path('logout/', views.logout),
]