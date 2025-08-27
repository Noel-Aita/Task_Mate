# tasks/filters.py
import django_filters
from .models import Task

class TaskFilter(django_filters.FilterSet):
    created_at_after = django_filters.DateTimeFilter(field_name="created_at", lookup_expr="gte")
    created_at_before = django_filters.DateTimeFilter(field_name="created_at", lookup_expr="lte")
    due_date_after = django_filters.DateTimeFilter(field_name="due_date", lookup_expr="gte")
    due_date_before = django_filters.DateTimeFilter(field_name="due_date", lookup_expr="lte")
    category_name = django_filters.CharFilter(field_name="category__name", lookup_expr="icontains")# filter by category name
    assigned_to_role = django_filters.CharFilter(field_name="assigned_to__role", lookup_expr="iexact") # fileter by assigned technician role

    class Meta:
        model = Task
        fields = ['status', 'priority', 'created_by', 'assigned_to', 'category']
