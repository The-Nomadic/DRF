from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='Index'),
    path('import-data/', views.import_students_from_excel, name='Import-Data'),
]