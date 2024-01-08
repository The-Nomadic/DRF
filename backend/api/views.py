from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import openpyxl
from .models import Student

# Create your views here.
def index(request):
    return HttpResponse("Welcome to my API Backend")

# Import Data
def import_students_from_excel(request):

    file_path = "/Programs/REST APIs/DRF/backend/students_data.xlsx"
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active

    # Get the fields of the Student model
    model_fields = [field.name for field in Student._meta.get_fields() if field.name != "id"]

    # Iterate over rows and create Student objects
    for row in sheet.iter_rows(min_row=2, values_only=True):
        student_data = dict(zip(model_fields, row))
        # print(student_data)
        Student.objects.create(**student_data)

    return HttpResponse("Import completed")