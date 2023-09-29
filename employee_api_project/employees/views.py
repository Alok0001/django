from django.http import JsonResponse
from .models import Employee  # Import the Employee model from your models.py file

def employee_list(request):
    # Creating four sample employee entries
    employees = [
        {"id": 1, "first_name": "John", "last_name": "Doe", "address": "123 Main St"},
        {"id": 2, "first_name": "Jane", "last_name": "Smith", "address": "456 Elm St"},
        {"id": 3, "first_name": "Alice", "last_name": "Johnson", "address": "789 Oak St"},
        {"id": 4, "first_name": "Bob", "last_name": "Williams", "address": "101 Pine St"},
    ]



    employee_list = []

    for employee_data in employees:
        employee_dict = {
            "id": employee_data["id"],
            "first_name": employee_data["first_name"],
            "last_name": employee_data["last_name"],
            "address": employee_data["address"],
        }
        employee_list.append(employee_dict)

    return JsonResponse({"employees": employee_list})
