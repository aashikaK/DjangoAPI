from django.contrib import admin
from django.urls import path,include

from .views import home_page
from rest_framework import routers
from .views import CompanyViewSet


router= routers.DefaultRouter()
router.register(r'companies',CompanyViewSet)
urlpatterns =[
    
    path("", include("router.urls"))
]