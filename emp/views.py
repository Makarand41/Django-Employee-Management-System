from django.shortcuts import render, redirect

# Create your views here.
# emp/views.py
from django.shortcuts import render
from django.http import HttpResponse

# emp/views.py
from django.http import HttpResponse

from emp.models import Emp

def emp_home(request):
    emps=Emp.objects.all()
    return render(request, "home.html",{
'emps':emps
    })

def add_emp(request):
    if request.method == "POST":
        # Fetch data from the form
        name = request.POST.get('name')

        phone = request.POST.get('phone')
        address = request.POST.get('address')
        working = bool(request.POST.get('working'))  # Convert to boolean
        department = request.POST.get('department')

        # Create an Emp object and save it to the database
        emp = Emp(name=name,  phone=phone, address=address, working=working, department=department)
        emp.save()

        print("Data has been added to the database")
        return redirect("/")

    return render(request,"add.html")


def delete_emp(request,emp_id):
    emp=Emp.objects.get(pk=emp_id)
    emp.delete()
    return redirect("/")

def update_emp(request,emp_id):
    emp=Emp.objects.get(pk=emp_id)
    return render(request, "update_emp.html",{
        'emp':emp
    })


def do_update_emp(request, emp_id):
    if request.method == 'POST':
        emp_name = request.POST.get("emp_name")
        emp_id_temp = request.POST.get("emp_id")
        emp_phone = request.POST.get("emp_phone")
        emp_address = request.POST.get("emp_address")
        emp_working = request.POST.get("emp_working")
        emp_department = request.POST.get("emp_department")

        e = Emp.objects.get(pk=emp_id)
        e.name = emp_name
        e.emp_id = emp_id_temp
        e.phone = emp_phone
        e.address = emp_address
        e.department = emp_department
        if emp_working is None:
            e.working = False
        else:
            e.working = True

        e.save()
    return redirect("/")
