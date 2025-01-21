from django.db import models

# Create your models here.
class Userprofile(models.Model):
    name = models.CharField(max_length = 50)
    email = models.EmailField(unique = True)
    contect=models.IntegerField()
    aadhar_no=models.IntegerField(unique=True)
    def __str__(self):
         return self.name

   
    

class Aadhar(models.Model):
      aadhar_no=models.IntegerField(unique=True)
      created_by=models.CharField(max_length=50)
      creted_data=models.DateField()
      aadhar_no=models.OneToOneField(Userprofile,on_delete=models.PROTECT)
      def __str__(self):
           return str(self.aadhar_no)


