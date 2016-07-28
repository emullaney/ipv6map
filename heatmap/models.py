from django.db import models


class ipv6Address(models.Model):
    network = models.CharField(max_length=255, blank=True)
    geoname_id = models.CharField(max_length=255, blank=True)
    postal_code = models.CharField(max_length=255, blank=True)
    latitude = models.FloatField(db_index=True, null=True, blank=True)
    longitude = models.FloatField(db_index=True, null=True, blank=True)

    class Meta:
        ordering = ('latitude', 'longitude', )
        verbose_name_plural = 'ipv6_addresses'