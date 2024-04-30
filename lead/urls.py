from django.contrib import admin
from django.urls import path, include
from .views import LeadViewset, delete_lead
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("leads", LeadViewset, basename="leads")

urlpatterns = [
    path('leads/delete_lead/<int:lead_id>/', delete_lead, name='delete_lead'),
    path("", include(router.urls)),
]
