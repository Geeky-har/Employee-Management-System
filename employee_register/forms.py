from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('name', 'empid', 'mobile_no', 'position')


    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)

        self.fields['position'].empty_label = 'Select'  # will display select in dropdown
        self.fields['empid'].required = False   # will non validate empid field
