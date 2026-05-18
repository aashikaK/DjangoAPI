from django.contrib import admin
from django.urls import path,include

from companyapi.views import home_page
from rest_framework import routers
from api.views import CompanyViewSet


router= routers.DefaultRouter()
router.register(r'companies',CompanyViewSet)
urlpatterns =[
    
    path("", include(router.urls))
]