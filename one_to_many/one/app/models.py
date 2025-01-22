from django.db import models


# Create your models here.
'''class Userprofile(models.Model):
     name=models.CharField(max_length=50)
     email=models.EmailField(unique=True)
     contact=models.IntegerField()
     aadhar_no=models.IntegerField(unique=True)


class Aadhar(models.Model):
      aadhar_no=models.IntegerField(unique=True)
      created_by=models.CharField(max_length=50)
      creted_data=models.DateField()
      aadhar_no=models.OneToOneField(Userprofile,on_delete=models.PROTECT) '''

response=[("HR","HR"),("Ec","Ec"),("Cs","Cs"),("Me","Me")]
class Department(models.Model):
    dep_name=models.CharField(unique=True,max_length=50)
    dep_des=models.TextField(max_length=50)
    dep_hod=models.CharField(max_length=100)
    def __str__(self):
        return self.dep_name

couces=[("1","B.tech"),("2","CBE"),("3","Bsc"),("4","MA")]
class Student(models.Model):
    std_name=models.CharField(max_length=40)
    std_email=models.EmailField()
    std_dep=models.ForeignKey(Department,on_delete=models.PROTECT,to_field='dep_name')
    std_roll=models.IntegerField()

    def __str__(self):
        return self.std_name
      





