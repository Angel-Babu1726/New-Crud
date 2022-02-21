from django.db import models

# Create your models here.
class Position(models.Model):
    Title=models.CharField(max_length=20,blank=False)

    def __str__(self):
        return self.Title

class Employee(models.Model):
    FullName=models.CharField(max_length=20,blank=False)
    Emp_code=models.CharField(max_length=20,blank=False)
    Mobilenum=models.CharField(max_length=10,blank=False)
    position=models.ForeignKey(Position,on_delete=models.CASCADE)

