from django.shortcuts import render,redirect,HttpResponseRedirect

from .models import user
from .form import EmployeeRegistration
# Create your views here.

# These  Function will add new data and show all data which is stored in database
def add_show(request):
    if request.method == 'POST':
        ob= EmployeeRegistration(request.POST)
        if ob.is_valid():
            ob.save()
            ob=EmployeeRegistration()      
    else:
        ob=EmployeeRegistration()    
    emp= user.objects.all()
    return render (request, 'addandshow.html', {'form':ob, 'emps':emp}) 


# These function work to update/edit data

def update_data(request,id):
 if request.method == 'POST':  
   dl = user.objects.get(pk=id)
   ob=EmployeeRegistration(request.POST, instance=dl) 
   if ob.is_valid():
    ob.save()
    ob=EmployeeRegistration()  
 else:
    dl = user.objects.get(pk=id)
    ob=EmployeeRegistration(instance=dl) 
 return render(request,"updateEmployee.html",{'form':ob})


# These function will delete the row data
def delete_data(request,id):
    if request.method == "POST":
        dl = user.objects.get(pk=id)
        dl.delete()
        return HttpResponseRedirect('/')

