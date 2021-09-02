from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.list),
    path('info/', views.info),
    path('review/', views.review),
    path('<userid>/', views.mypage),
    # path('mypage/', views.mypage),


]