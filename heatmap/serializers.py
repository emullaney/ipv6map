from django.contrib.auth.models import User, Group
from rest_framework import serializers

from heatmap.models import ipv6Address


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class ipv6AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ipv6Address
        fields = ('network', 'geoname_id', 'postal_code', 'latitude', 'longitude')