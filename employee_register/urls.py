from django.urls import path, include
from employee_register import views

urlpatterns = [
    # get request for new employee registration
    path('/form', views.employee_form, name='employee_reg'),

    # post request to update the details of employees
    path('/form/<int:id>/', views.employee_form, name='employee_update'),

    # post request to update the details of employees (will carry id in the url)
    path('/delete/<int:id>/', views.employee_delete, name='employee_delete'),

    # get request to view the list of employees and their corresponding details
    path('/list', views.employee_list, name='employee_list')

]