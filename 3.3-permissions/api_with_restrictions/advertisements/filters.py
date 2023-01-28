from django_filters import rest_framework as filters, DateFromToRangeFilter, FilterSet

from advertisements.models import Advertisement


class AdvertisementFilter(FilterSet):
    """Фильтры для объявлений."""

    # TODO: задайте требуемые фильтры
    created_at = DateFromToRangeFilter()
    class Meta:
        model = Advertisement
        fields = ['created_at']
