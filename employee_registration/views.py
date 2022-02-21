from django.shortcuts import redirect,render

from .models import Employee
from . forms import Empform

# Create your views here.
def employee_list(request):
    context={'employee_list': Employee.objects.all()}
    return render(request,"employee_list.html", context)

def employee_form(request,id=0):
    if request.method == "GET":
        if id == 0:
            form=Empform()
        else:
            employee = Employee.objects.get(pk=id) 
            form = Empform(instance=employee)
        return render(request, "employee_form.html", {'k': form})
        
    else:
        if id == 0:
            form = Empform(request.POST)
        else: 
            employee = Employee.objects.get(pk=id)
            form = Empform(request.POST,instance= employee)
        if form.is_valid(): 
            form.save()
        return redirect('/list') 


def employee_delete(request,id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/list')






