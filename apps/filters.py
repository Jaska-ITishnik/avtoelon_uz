from apps.models import Adv
from django_filters import BooleanFilter, FilterSet


class AdvFilterSet(FilterSet):
    is_barging = BooleanFilter(method='get_is_barging')

    class Meta:
        model = Adv
        fields = 'is_barging',

    def get_is_barging(self, queryset, value, name):
        if name:
            return Adv.objects.filter(is_barging=True)
        return Adv.objects.all()
