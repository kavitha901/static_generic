from django.db import models

# Create your models here.
class Dept(models.Model):
    deptno=models.IntegerField(primary_key=True)
    dname=models.CharField(max_length=100)
    dloc=models.CharField(max_length=100)
    def __str__(self):
        return self.dname
class Emp(models.Model):
    deptno=models.ForeignKey(Dept,on_delete=models.CASCADE)
    empno=models.IntegerField(primary_key=True)
    ename=models.CharField(max_length=100)
    sal=models.DecimalField(max_digits=10,decimal_places=2)
    job=models.CharField(max_length=100)
    comm=models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    hiredate=models.DateField(auto_now_add=True)
    mgr=models.ForeignKey('self',on_delete=models.SET_NULL,null=True,blank=True)
class SalGrade(models.Model):
    grade=models.IntegerField(primary_key=True)
    hisal=models.DecimalField(max_digits=10,decimal_places=2)
    losal=models.DecimalField(max_digits=10,decimal_places=2)
    