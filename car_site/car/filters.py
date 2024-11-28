from django_filters import FilterSet
from .models import *

class CarFilter(FilterSet):
    class Meta:
        model = Car
        fields = {
            'car_mark': ['exact'],
            'year': ['gt', 'lt'],
        }