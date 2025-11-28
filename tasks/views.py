from django.shortcuts import render
from django.http import HttpResponse
from tasks.forms import TaskForm
from tasks.models import Employee
# Create your views here.
def user_dashboard(request):
    return render(request,"dashboard/user_dashboard.html")
def manager_dashboard(request):
    return render(request,"dashboard/manager.html")
def dashboard(request):
    return render(request,"dashboard/dashboard.html")
def test(request):
    return render(request,'test.html')

def create_task(request):
    employees = Employee.objects.all()
    form = TaskForm(employees=employees)
    context = {"form":form}
    return render(request,'task_form.html',context)