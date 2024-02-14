import datetime

import django_filters
from django.utils import timezone

from dataset.models import Dataset

DATE_FORMAT = '%Y-%m-%d'


class DatasetFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(lookup_expr='icontains')
    firstname = django_filters.CharFilter(lookup_expr='icontains')
    lastname = django_filters.CharFilter(lookup_expr='icontains')
    email = django_filters.CharFilter(lookup_expr='icontains')
    age = django_filters.NumberFilter(method='age_filter')
    age__gt = django_filters.NumberFilter(method='age_filter__gt')
    age__lt = django_filters.NumberFilter(method='age_filter__lt')
    birthDate__gte = django_filters.DateFilter(method='birthDate__gt_filter')
    birthDate__lte = django_filters.DateFilter(method='birthDate__lt_filter')
    gender = django_filters.CharFilter(method='gender_filter')

    class Meta:
        model = Dataset
        fields = ['category', 'firstname', 'lastname', 'email', 'gender', 'birthDate']

    def gender_filter(self, queryset, name, value):
        if value.isdigit():
            return queryset.filter(**{
                name: value,
            })

        else:
            choice = Dataset.Gender.UNKNOWN
            for c in Dataset.Gender.choices:
                if value.lower() == c[1].lower():
                    choice = c[0]
            return queryset.filter(**{
                name: choice,
            })

    def birthDate__gt_filter(self, queryset, name, value):
        try:

            return queryset.filter(**{
                name: value
            })
        except:
            return queryset

    def birthDate__lt_filter(self, queryset, name, value):
        try:
            return queryset.filter(**{
                name: value
            })
        except:
            return queryset

    def age_filter(self, queryset, name, value):
        days_per_year = 365.24
        try:
            return queryset.filter(**{
                "birthDate__year": datetime.datetime.date(
                    timezone.now() - datetime.timedelta(days=(int(value) * days_per_year))).year
            })
        except:
            return queryset

    def age_filter__gt(self, queryset, name, value):
        days_per_year = 365.24
        try:
            return queryset.filter(**{
                "birthDate__year__lte": datetime.datetime.date(
                    timezone.now() - datetime.timedelta(days=(int(value) * days_per_year))).year
            })
        except:
            return queryset

    def age_filter__lt(self, queryset, name, value):
        days_per_year = 365.24
        try:
            return queryset.filter(**{
                "birthDate__year__gte": datetime.datetime.date(
                    timezone.now() - datetime.timedelta(days=(int(value) * days_per_year))).year
            })
        except:
            return queryset
