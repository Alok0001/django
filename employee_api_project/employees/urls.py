
from django.urls import path
from .views import employee_list  # Import the employee_list view

urlpatterns = [
    path('employees/', employee_list, name='employee-list'),  # Map the view to the URL pattern
]
