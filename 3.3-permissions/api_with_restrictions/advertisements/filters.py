from django_filters import rest_framework as filters, DateFromToRangeFilter, FilterSet, CharFilter, ModelChoiceFilter

from advertisements.models import Advertisement


class AdvertisementFilter(FilterSet):
    """Фильтры для объявлений."""

    # TODO: задайте требуемые фильтры
    created_at = DateFromToRangeFilter(field_name='created_at')
    status = CharFilter(field_name='status')
    creator = ModelChoiceFilter(field_name='creator')
    class Meta:
        model = Advertisement
        fields = ['created_at', 'status', 'creator']
