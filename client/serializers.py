from rest_framework import serializers
from .models import *


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
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
            "name",
            "contact_person",
            "email",
            "phone",
            "website",
            "created_by",
            "created_at",
            "modified_at",
        )


class NotesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Note
        read_only_fields = (
            "team",
            "client",
            "created_by",
            "created_at",
            "modified_at",
        )
        fields = (
            "id",
            "team",
            "client",
            "name",
            "body",
            "created_by",
            "created_at",
            "modified_at",
        )
