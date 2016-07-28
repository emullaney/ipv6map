from django.contrib.auth.models import User, Group
from django.shortcuts import render
from django.views.generic import View

from rest_framework import viewsets

from heatmap.serializers import UserSerializer, GroupSerializer, ipv6AddressSerializer
from heatmap.models import ipv6Address


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class ipv6AddressViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = ipv6Address.objects.all()
    serializer_class = ipv6AddressSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned addresses
        based on filters passed in
        """
        queryset = ipv6Address.objects.all()
        # Filter by postal code
        postal_code = self.request.query_params.get('postal_code', None)
        if postal_code:
            queryset = queryset.filter(postal_code=postal_code)
        # Filter by max latitude
        max_latitude = self.request.query_params.get('max_latitude', None)
        if max_latitude:
            queryset = queryset.filter(latitude__lte=max_latitude)
        # Filter by min latitude
        min_latitude = self.request.query_params.get('min_latitude', None)
        if min_latitude:
            queryset = queryset.filter(latitude__gte=min_latitude)
        # Filter by max longitude
        max_longitude = self.request.query_params.get('max_longitude', None)
        if max_longitude:
            queryset = queryset.filter(longitude__lte=max_longitude)
        # Filter by min longitude
        min_longitude = self.request.query_params.get('min_longitude', None)
        if min_longitude:
            queryset = queryset.filter(longitude__gte=min_longitude)
        return queryset


class MapView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'map.html', {
        'data': "test",
        })
