from django.shortcuts import render
from .models import Student

# Create your views here.


def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
    
        name=request.POST.get('username')
        email=request.POST.get('email')
        detail=request.POST.get('detail')
        phone=request.POST.get('phone')
        dob=request.POST.get('dob')
        subscribe=request.POST.getlist('subscribe')
        gender=request.POST.get('gender')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')
        profile_pic=request.POST.get('profile-pic')
        resume=request.POST.get('resume')
        print(request.POST)
        print(request.FILES)
        print(name,email,detail,phone,dob,subscribe,gender,password,cpassword,profile_pic,resume)
        user = Student.objects.filter(email=email)
        if user:
            x = "Email already exist"
            return render(request, 'register.html', {'msg': x})
        else:
            if password==cpassword:
                Student.objects.create(name=name,email=email,detail=detail,phone=phone,dob=dob,subscribe=subscribe,gender=gender,profile_pic=profile_pic,resume=resume)
        
                x="Registration Successfully"
                return render(request,'logon.html',{'mag':x})
            

            else:
                z='password and cpassword not match'
                return render(request,'register.html',{'msg':z,'name':name,'email':email,'detail':detail,'phone':phone,'dob':dob,'subscribe':subscribe,'gender':gender,'profile_pic':profile_pic,'resume':resume})
  
    else:
     return render(request, 'register.html')
def login(request):
    if request.method=='POST':
        email=request.POST.get('email')
        passward=request.POST.get('passward')
        print(email,passward)
        user=Student.objects.filter(email=email)
        if user:
            data=Student.objects.get(email=email)
            #   print(data.name)
            #   print(data.email)
            #   print(data.detail)
            #   print(data.phone)
            #   print(data.subscribe)
            #   print(data.gender)
            #   print(data.dob)
            #   print(data.profile_pic)
            #   print(data.resume)
            #   print(data.password)
            pass1= data.password
            print(pass1,passward)
            if pass1 == passward:
                return render(request,'dashboard.html',{'name':data.name,'email':data.email})
            else:
                msg = "Enter and Password not Match"
                return render(request,'login.html',{'msg':msg})
        else:
            msg = "Email not Exist"
            return render(request,'register.html',{'msg':msg})
           
    else:
       return render(request, 'login.html')
           





