import django_filters
from .models import *


class questionfilter(django_filters.FilterSet):
    class Meta:
        model = Contact
        fields = ['user','sent_at']