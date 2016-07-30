from rest_framework import serializers

from heatmap.models import ipv6Address


class ipv6AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ipv6Address
        fields = ('network', 'geoname_id', 'postal_code', 'latitude', 'longitude')