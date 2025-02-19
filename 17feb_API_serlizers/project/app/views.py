from django.shortcuts import render
from.models import Student
# Create your views here.
from django.http import HttpResponse,JsonResponse
from .serializers import Stu_Serializers
from rest_framework.renderers import JSONRenderer

def index(request):
    return render(request,'index.html')
def student_list(req):
    stu=Student.objects.all()
    print(stu)
    serializer=Stu_Serializers(stu,many=True)
    print("serializer=",serializer)
    print(serializer.data)
    json_data=JSONRenderer().render(serializer.data)
    print("json_data=",json_data)
    return HttpResponse(json_data,content_type='application/json')
def student_details(req,pk):
    user=Student.objects.get(id=pk)
    serilizer=Stu_Serializers(user)
    print("serilizer=",serilizer)
    print(serilizer.data)
    return JsonResponse(serilizer.data,safe=False)




