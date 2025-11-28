from django.shortcuts import render
from django.http import HttpResponse
from tasks.forms import TaskForm
from tasks.models import Employee,Task
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
    if request.method=="POST":
        form = TaskForm(request.POST,employees=employees)
        if form.is_valid():
            data = form.cleaned_data
            title = data.get("title")
            description = data.get("description")
            due_date = data.get("due_date")
            assigned_to = data.get("assigned_to")
            task = Task.objects.create(title=title,description=description,due_date=due_date)
            for emp_id in assigned_to:
                employee = Employee.objects.get(id=emp_id)
                task.assign_to.add(employee)

        
    
    context = {"form":form}
    return render(request,'task_form.html',context)