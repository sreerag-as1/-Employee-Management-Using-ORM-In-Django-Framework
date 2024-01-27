from django.shortcuts import render, redirect
from .models import Employee
from django.http import HttpResponse

# Create your views here.
def create_employee(request):
    #How to check incoming request is GET/POST???
    if request.method == 'GET':
        return render(request, 'empapp/employee_form.html')
    elif request.method == 'POST':

# Step 1 : Read Employee input data

        emp_id = request.POST.get('emp_id')
        name = request.POST.get('emp_name')
        age = request.POST.get('emp_age')
        salary = request.POST.get('emp_salary')
        address = request.POST.get('emp_address')

# Step 2 : Create Employee Model Object using Employee input data

        employee = Employee(empid=emp_id, name=name, age=age, salary=salary, address=address)

# Step 3 : Call save() method on Employee Model Object

        employee.save()

# Step 4 : Return response to client saying that Employee created successfully

    return HttpResponse("<h1 style='color : green'>Employee Created Successfully</h1>")

def list_employees(request):
    #Step 1 : x = Get all employees from Database table (EMPLOYEE) ==> QuerySet
    # employees = {emp1, emp2}
    employees_db = Employee.objects.all()

    #Step 2 : Create Context Object (Dictionary) with QuerySet
    context_data = {
        "employees" : employees_db
    }

    #Step 3 : Send Context Object through render() function
    return render(request, 'empapp/list_emp.html', context=context_data)

def delete_emp(request):
    if request.method == 'GET':
        return render(request, 'empapp/del_emp_form.html')
    elif request.method == 'POST':

        #Step 1 : Read the Input Employee ID to be Deleted

        id_input = request.POST.get('emp_pk')

        #Step 2 : Get Employee Object from DB based on Input Employee ID.. Employee Model Object

        try:
            employee = Employee.objects.get(id=id_input)

        #Step 3 : Call delete() on top of Employee Model Object, Employee will be deleted from DB

            employee.delete()
            resp_msg = "h1 style='color : green'>Employee Deleted Successfully</h1>"

        except Exception:
                resp_msg = '<h1 style="color : red">Ops! Employee with ID {} did not found</h1>'.format(id_input)

        #Step 4 : Send Success Response back to the Client

        return HttpResponse(resp_msg)

def ems(request):
    if request.method == 'GET':

        employees_db  = Employee.objects.all()

        context_data = {
            "employees" : employees_db
        }

        return render(request, 'empapp/ems.html', context=context_data)
    elif request.method == 'POST':

        empid = request.POST.get('emp_id')
        name = request.POST.get('emp_name')
        age = request.POST.get('emp_age')
        salary = request.POST.get('emp_salary')
        address = request.POST.get('emp_address')

        employee = Employee(empid=empid, name=name, age=age, salary=salary, address=address)

        employee.save()

        return redirect('/empapp/ems/')

def update_employee(request, pk):
    employee_db = Employee.objects.get(id=pk)

    employee_db.empid = request.POST.get("emp_id")
    employee_db.name = request.POST.get("emp_name")
    employee_db.age = request.POST.get("emp_age")
    employee_db.salary = request.POST.get("emp_salary")
    employee_db.address = request.POST.get("emp_address")

    employee_db.save()
    return redirect('/empapp/ems/')

def delete_employee(request, pk):
    employee = Employee.objects.get(id=pk)
    employee.delete()
    return redirect('/empapp/ems/')
