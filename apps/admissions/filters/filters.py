import django_filters
from apps.admissions.models import Internacao


class InternacaoFilter(django_filters.FilterSet):
    
    data_alta__isnull = django_filters.BooleanFilter(
        field_name='data_alta',
        lookup_expr='isnull',
        label='Sem alta (internação em aberto)'
    )

    class Meta:
        model = Internacao
        fields = {
            'data_alta': ['exact', 'gte', 'lte'],
            'leito': ['exact'],
            'paciente': ['exact'],
            'is_active': ['exact'],
            # Adicione outros campos que você quiser filtrar
        }