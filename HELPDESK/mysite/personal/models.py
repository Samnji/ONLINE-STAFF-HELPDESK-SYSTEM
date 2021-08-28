from django.db import models

# Create your models here.

class Employee(models.Model):
	Emp_Id=models.CharField(max_length=10, unique=True)
	F_Name=models.CharField(max_length=15)
	L_Name=models.CharField(max_length=15)
	Birth_date=models.CharField(max_length=10, help_text="Date of Birth")
	Gender=models.CharField(max_length=10)
	Salary=models.CharField(max_length=10)
	def __str__(self):
         return self.F_Name + " " + self.L_Name


class Helpdesk_Support_team(models.Model):
	HDS_Id=models.CharField(max_length=10, unique=True)
	F_Name=models.CharField(max_length=15)
	L_Name=models.CharField(max_length=15)
	Birth_date=models.CharField(max_length=10, help_text="Date of Birth")
	Gender=models.CharField(max_length=10)
	Salary=models.CharField(max_length=10)
	def __str__(self):
         return self.F_Name + " " + self.L_Name



class Manager(models.Model):
	Manager_Id=models.CharField(max_length=10, unique=True)
	F_Name=models.CharField(max_length=15)
	L_Name=models.CharField(max_length=15)
	Birth_date=models.CharField(max_length=10, help_text="Date of Birth")
	Gender=models.CharField(max_length=10)
	Salary=models.CharField(max_length=10)
	def __str__(self):
         return self.F_Name + " " + self.L_Name


class Supervisor(models.Model):
	Sup_Id=models.CharField(max_length=10, unique=True)
	F_Name=models.CharField(max_length=15)
	L_Name=models.CharField(max_length=15)
	Birth_date=models.CharField(max_length=10, help_text="Date of Birth")
	Gender=models.CharField(max_length=10)
	Salary=models.CharField(max_length=10)
	def __str__(self):
         return self.F_Name + " " + self.L_Name


class Task(models.Model):
	No=models.CharField(max_length=15, unique=True)
	F_Name=models.CharField(max_length=15)
	L_Name=models.CharField(max_length=15)
	task=models.TextField(max_length=100)
	
	def __str__(self):
         return self.F_Name + " " + self.L_Name
 

class Staff(models.Model):
	No=models.CharField(max_length=15, unique=True)
	F_Name=models.CharField(max_length=15)
	L_Name=models.CharField(max_length=15)
	Staff_Role=models.TextField(max_length=30)
	Gender=models.CharField(max_length=10)
	
	def __str__(self):
         return self.F_Name + " " + self.L_Name