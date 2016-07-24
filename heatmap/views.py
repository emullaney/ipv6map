from django.contrib.auth.models import User, Group
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
