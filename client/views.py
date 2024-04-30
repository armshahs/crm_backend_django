from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render

from rest_framework import viewsets, status, filters
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *
from .models import *
from lead.models import Lead
from team.models import Team


# Create your views here.


class ClientPagination(PageNumberPagination):
    page_size = 5


class ClientViewset(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
    pagination_class = ClientPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ("name", "contact_person")

    def get_queryset(self):
        # adding this to get list of all teams where you are a part, not necessary that you have created it.
        team = Team.objects.filter(members__in=[self.request.user]).first()
        # return self.queryset.filter(created_by=self.request.user)
        return self.queryset.filter(team=team)

    # adding this to only automatically override and save the current user in the created_by field.
    def perform_create(self, serializer):
        # similar to get+queryset, this needs to be assigned to a team as well.
        team = Team.objects.filter(members__in=[self.request.user]).first()
        return serializer.save(team=team, created_by=self.request.user)


class NoteViewSet(viewsets.ModelViewSet):
    serializer_class = NotesSerializer
    queryset = Note.objects.all()

    def get_queryset(self):
        # adding this to get list of all teams where you are a part, not necessary that you have created it.
        team = Team.objects.filter(members__in=[self.request.user]).first()
        # gets the client field from the Get response, data obtained from query string
        client_id = self.request.GET.get("client_id")
        # return self.queryset.filter(created_by=self.request.user)
        return self.queryset.filter(team=team).filter(client_id=client_id)

    # adding this to only automatically override and save the created_by & client fileds in the Db.
    def perform_create(self, serializer):

        # similar to get_queryset, this needs to be assigned to a team as well as client.
        team = Team.objects.filter(members__in=[self.request.user]).first()
        # get client field from frontend request, data obtained from response body
        client_id = self.request.data["client_id"]

        return serializer.save(
            team=team, created_by=self.request.user, client_id=client_id
        )


@api_view(["POST"])
def convert_lead_to_client(request):
    # creating team filter because we want it to be restricted to a team
    team = Team.objects.filter(members__in=[request.user]).first()

    # fetching the lead_id from the request body from frontend
    lead_id = request.data["lead_id"]

    # Obtaining the lead details from the 'lead' table by fetching using
    # the primary key obtained from the request body key 'lead_id'
    try:
        lead = Lead.objects.filter(team=team).get(pk=lead_id)
    except Lead.DoesNotExist:
        raise Http404

    # creating a new entry in the "client" table using the lead details
    # obtained from the "lead" table
    client = Client.objects.create(
        team=team,
        name=lead.company,
        contact_person=lead.contact_person,
        email=lead.email,
        phone=lead.phone,
        website=lead.website,
        created_by=request.user,
    )

    return Response()


@api_view(['POST'])
def delete_client(request, client_id):
    team = Team.objects.filter(members__in=[request.user]).first()

    client = team.clients.filter(pk=client_id)
    client.delete()

    return Response({'message': 'The client was deleted'})