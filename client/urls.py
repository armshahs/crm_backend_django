from django.contrib import admin
from django.urls import path, include
from .views import ClientViewset, NoteViewSet, convert_lead_to_client, delete_client
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("clients", ClientViewset, basename="clients")
router.register("notes", NoteViewSet, basename="notes")

urlpatterns = [
    path("convert_lead_to_client/", convert_lead_to_client, name="convert_lead_to_client"),
    path('clients/delete_client/<int:client_id>/', delete_client, name='delete_client'),
    path("", include(router.urls)),
]
