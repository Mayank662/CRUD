from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.emp_form, name = 'employee_insert'),  # Get and post req. for insert operation
    path('<int:id>/', views.emp_form, name = 'employee_update'),  # Get and post req. for Update operation
    path('delete/<int:id>/',views.emp_delete,name='employee_delete'),
    path('list/', views.emp_list, name='employee_list')  # Get and post req. to retrieve and display all records
]
