from django.shortcuts import render, HttpResponse, redirect
from .forms import EmployeeForm
from .models import Employee
from django.contrib import messages

# Create your views here.

def employee_form(request, id=0):
    if request.method == 'GET':

        if id == 0: # means new registration page is running
            form = EmployeeForm()

        else:   # means update needs to take place(to fill the existing form)

            # will return the object having the specified id
            employee = Employee.objects.get(pk=id)

            # will pass the object the constructor of our model form
            form = EmployeeForm(instance=employee)

        return render(request, 'employee_form.html', {'form':form})

    else:   # when request is post

        if id == 0: # new registration page is running

            isUpdate = False

            # will store the details of the form fields
            form = EmployeeForm(request.POST)

        else:   # means update needs to take place

            isUpdate = True

            # will return the object containing the specified id
            employee = Employee.objects.get(pk=id)

            # will store the details of the form fields
            form = EmployeeForm(request.POST, instance=employee)

        # will check if the form details are valid or not

        if form.is_valid():
            form.save() # will save the details to the db

            # block for alert

            if isUpdate:
                messages.success(request, 'Record is Successfully updated')

            else:
                messages.success(request, 'New record is successfully added')

        return redirect('/employee/list')

def employee_list(request):

    # will store all the objects of employees stored in the db

    context = { 'employee_list': Employee.objects.all() }

    # will send the list of objects to our markup

    return render(request, 'employee_list.html', context)

def employee_delete(request, id):

    # will return the object containing the specified id
    employee = Employee.objects.get(pk=id)

    # will delete the record
    employee.delete()

    return redirect('/employee/list')