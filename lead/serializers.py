from rest_framework import serializers
from .models import *
from team.serializers import UserSerializer


class LeadSerializer(serializers.ModelSerializer):
    assigned_to = UserSerializer(read_only=True)
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Lead
        # ensuring that some fields are read only and do not need to be passed.
        # Also for the created_by to be automatically picked, add def perform_create in views
        read_only_fields = (
            "created_by",
            "created_at",
            "modified_at",
        )
        fields = (
            "id",
            "team",
            "company",
            "contact_person",
            "email",
            "phone",
            "website",
            "confidence",
            "estimated_value",
            "priority",
            "assigned_to",
            "created_by",
            "created_at",
            "modified_at",
        )
