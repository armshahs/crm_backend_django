from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import viewsets, status, filters
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from djangoCRM.pagination import CustomPagination
from .serializers import *
from .models import *
from team.models import Team

# Create your views here.


# class LeadPagination(PageNumberPagination):
#     page_size = 10


class LeadViewset(viewsets.ModelViewSet):
    serializer_class = LeadSerializer
    queryset = Lead.objects.all()
    pagination_class = CustomPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ("company", "contact_person")

    def get_queryset(self):
        # adding this to get list of all teams where you are a part, not necessary that you have created it.
        team = Team.objects.filter(members__in=[self.request.user]).first()
        # return self.queryset.filter(created_by=self.request.user)
        return self.queryset.filter(team=team)

    def perform_update(self, serializer):
        # get the current lead
        obj = self.get_object()

        # get assigned_to field from frontend request
        member_id = self.request.data["assigned_to"]

        if member_id:
            user = User.objects.get(pk=member_id)
            serializer.save(assigned_to=user)
        else:
            serializer.save()  # no user gets assigned

    # adding this to only automatically override and save the current user in the created_by field.
    def perform_create(self, serializer):
        # similar to get+queryset, this needs to be assigned to a team as well.
        team = Team.objects.filter(members__in=[self.request.user]).first()
        return serializer.save(team=team, created_by=self.request.user)


@api_view(['POST'])
def delete_lead(request, lead_id):
    team = Team.objects.filter(members__in=[request.user]).first()
    # print(team)
    # print(team.leads.all())
    lead = team.leads.filter(pk=lead_id)
    # print(lead)
    lead.delete()

    return Response({'message': 'The lead was deleted'})