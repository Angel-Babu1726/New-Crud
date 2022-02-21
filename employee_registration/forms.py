from turtle import position
from django.forms import ModelForm
from . models import Employee


class Empform(ModelForm):
    class Meta:
        model=Employee
        fields='FullName','Mobilenum','Emp_code','position'
        labels={'FullName':'Name','Emp_code':'Employee_ID','Mobilenum':'Phone_no','position':'Position'}
