from django.shortcuts import render
from.models import Student


# Create your views here.
def home(request):
    stu=Student.objects.all()
    print(stu)
    return render(request,'home.html',{'data':stu.values})

def delete(request,pk):
    data=Student.objects.get(id=pk)
    data.delete()
    stu=Student.objects.all()
    return render(request, 'home.html',{'data':stu})

def edit(request,pk):
    data= Student.objects.get(id=pk)
    stu=Student.objects.all()
    return render(request, 'home.html',{'data':stu,'data1':data})

def updatedat(request,pk):
    if request.method=="POST":
        x = Student.objects.get(id=pk)
        p = request.POST.get('name')
        q = request.POST.get('email')
        r = request.POST.get('city')
        s = request.POST.get('contact')
        x.stu_city = r
        x.stu_contact = s
        x.stu_email = q
        x.stu_name = p
        x.save()
        stu=Student.objects.all()
        return render(request, 'home.html',{'data':stu})

