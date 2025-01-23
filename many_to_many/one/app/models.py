from django.db import models

# Create your models here.
v_nm=[('Tata','Tata'),('bmw','bmw'),('Audi','Audi')]
f_nm=[('petrol','petrol'),('Desal','Desal'),('CNG','CnG'),('EV','EV')]
class Vehical(models.Model):
      v_name=models.CharField(max_length=50,choices=v_nm)
      def __str__(self):
            return self.v_name


class Fuel(models.Model):
    f_name=models.CharField(max_length=50,choices=f_nm)
    v_name=models.ManyToManyField(Vehical)
    def __str__(self):
         return self.f_name
    