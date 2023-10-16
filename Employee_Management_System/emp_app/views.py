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

def add_emp(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        role = int(request.POST['role'])
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        phone = int(request.POST['phone'])
        dept = int(request.POST['department'])
        new_emp = Employee(first_name=first_name, last_name=last_name, salary=salary, bonus=bonus, phone=phone, dept_id = dept, role_id = role, hire_date= datetime.now())
        new_emp.save()
        return HttpResponse('Employee added Successfully..!')
    else: 
        return render(request, 'add_emp.html')

def remove_emp(request):
    if request.method == 'POST':
        
        try:
            if 'delete_selected' in request.POST:
                selected_emp_id = request.POST.getlist('employee_ids')
                Employee.objects.filter(id__in = selected_emp_id).delete()
                print('in deleted')
                return HttpResponse("Selected Employees detail is deleted successfully..")
            
            if request.POST['emp-id']:
                emp_id = request.POST['employee_id']
                emps = Employee.objects.filter(id = emp_id)
                print('in emp id')
                return render(request, 'remove_emp.html', {'employee': emps})
            
            print('here')
            if 'emp-role' in request.POST:
                employees = []
                print("heee")
                emps_role = request.POST['emp_role']
                
                lst_emps = Employee.objects.filter(role = emps_role)
                print("The id is " , lst_emps)
            print('in last view')
        except:
            pass
            # return HttpResponse("Enter the correct Input")


    return render(request, 'remove_emp.html')

def filter_emp(request):
    return render(request, 'filter_emp.html')








