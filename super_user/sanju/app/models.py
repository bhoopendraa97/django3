from django.db import models

# Create your models here.
class Employee(models.Model):
    s_no = models.AutoField(primary_key = True)
    emp_name = models.CharField(max_length = 50)
    emp_email = models.EmailField(unique = True)
    emp_joining_date = models.DateTimeField(auto_now_add=True)
    emp_updated_at = models.DateTimeField(auto_now=True)
    emp_dob = models.DateTimeField()
    emp_start_time = models.TimeField()
    emp_active = models.BooleanField()
    emp_discription = models.TextField()
    emp_pic = models.ImageField(upload_to='image/')
    emp_document = models.FileField(upload_to='file/')

		
    