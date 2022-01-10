from django.shortcuts import redirect, render
from .forms import EmpForm
from .models import Emp

# Create your views here.
def emp_list(request):
    context = {'emp_list':Emp.objects.all()}
    return render(request,"emp_register/emp_list.html",context)

def emp_form(request, id=0):
    if request.method =="GET":
        if id==0:
            form = EmpForm()
        else:
            emp = Emp.objects.get(pk=id)
            form = EmpForm(instance=emp)
        return render(request,"emp_register/emp_form.html",{'form':form})
    else:
        if id == 0:
            form = EmpForm(request.POST)
        else:
            employee = Emp.objects.get(pk=id)
            form = EmpForm(request.POST, instance = employee)
        if form.is_valid():
            form.save()
        return redirect('/employee/list')

def emp_delete(request,id):
    employee = Emp.objects.get(pk=id)
    employee.delete()
    return redirect('/employee/list')
