from django.urls import path
from app1 import views

my_app="app1"

urlpatterns = [
    path('',views.base,name='base'),
    path('home/',views.home,name='home'),
    path('dept/',views.department,name='department'),
    path('place/',views.placement,name='placement'),
    path('contact/',views.contact,name='contact'),
]