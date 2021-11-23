from django.db.models import fields
import django_filters
from django_filters.filters import DateFilter
from .models import *
class OrderFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name='created_date',lookup_expr='gte')
    end_date = DateFilter(field_name='created_date',lookup_expr='lte')
    class Meta :
        model = Order
        fields = "__all__"
        exclude = ['customer','created_date']