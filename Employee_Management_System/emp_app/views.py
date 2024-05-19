from django.shortcuts import render, HttpResponse
from .models import Employee, Role, Department
from datetime import datetime


# Create your views here.

def index(request):
    return render(request, 'index.html')

def all_emp(request):
    emps = Employee.objects.all()
    context = {'emps': emps}
    return render(request, 'all_emp.html', context)

from .models import Department, Role

def add_emp(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        role_id = int(request.POST['role'])
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        phone = int(request.POST['phone'])
        dept_id = int(request.POST['department'])
        new_emp = Employee(first_name=first_name, last_name=last_name, salary=salary, bonus=bonus, phone=phone, dept_id=dept_id, role_id=role_id, hire_date=datetime.now())
        new_emp.save()
        return render(request, 'add_emp.html', {"text": "Employee Added Successfully..!"})
    elif request.method == 'GET':
        departments = Department.objects.all()
        roles = Role.objects.all()
        return render(request, 'add_emp.html', {'departments': departments, 'roles': roles})
    else: 
        return render(request, 'add_emp.html', {"text": "An error Occurred! Employee has not been Added...!"})

        


def remove_emp(request):
    if request.method == 'POST':
        emps = Employee.objects.all()
        employee_id_str = request.POST.get('get_emp')
        print(employee_id_str, type(employee_id_str))
        if not employee_id_str.isdigit():
            return render(request, 'remove_emp.html', {"con": "Invalid employee ID. Please enter a valid number."})
        
        employee_id = int(employee_id_str)

        if emps.filter(id=employee_id).exists():
            Employee.objects.filter(id=employee_id).delete()
           
            return render(request, 'remove_emp.html', {"con": "Employee successfully deleted."})
        else:
            return render(request, 'remove_emp.html', {"con": "Employee not found. Please enter a correct ID."})

    return render(request, 'remove_emp.html', {"con": "Enter ID"})



def filter_emp(request):
    context = {"all_roles":Role.objects.all(), "all_location": Department.objects.all()}

    if request.method == 'POST':
        name = request.POST['first_name']
        role = request.POST['role']
        location = request.POST['loc']
        employee = Employee.objects.all()

        if name:
            employee = employee.filter(first_name__icontains=name)
        if role:
            employee = employee.filter(role__name = role)
        if location:
            employee = employee.filter(dept__location =  location)
        context['emps'] = employee
        
        return render(request, "filter_emp.html", context)
    
    return render(request, 'filter_emp.html', context)




