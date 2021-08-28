from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class MyAccountManager(BaseUserManager):
	def create_user(self, staff_id, first_name, last_name, password=None):
		if not staff_id:
			raise ValueError("Users must have a staff_id")
		if not first_name:
			raise ValueError("Users must have a first_name")
		if not last_name:
			raise ValueError("Users must have a last_name")

		user  = self.model(
			staff_id=staff_id,
			first_name=first_name,
			last_name=last_name,

			)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, staff_id, first_name, last_name, password=None):
		user  = self.create_user(
			staff_id=staff_id,
			first_name=first_name,
			last_name=last_name,
			password=password,

			)

		user.is_admin= 		True
		user.is_staff= 		True
		user.is_superuser=  True
		user.save(using=self._db)
		return user
		
class Account(AbstractBaseUser):

	staff_id     = models.CharField(verbose_name="staff_id", max_length=10, unique=True)
	first_name   = models.CharField(verbose_name="first_name", max_length=15)
	last_name    = models.CharField(verbose_name="last_name", max_length=15)
	date_joined  = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
	last_login   = models.DateTimeField(verbose_name="last login", auto_now=True)
	is_admin     = models.BooleanField(default=False)
	is_active    = models.BooleanField(default=True)
	is_staff 	 = models.BooleanField(default=False)
	is_superuser = models.BooleanField(default=False)
	


	USERNAME_FIELD	= 'staff_id'
	REQUIRED_FIELDS = ['first_name', 'last_name']


	objects=MyAccountManager()


	def __str__(self):
		return self.staff_id 
	def has_perm(self, perm, object=None):
		return self.is_admin

	def has_module_perms(self, app_label):
		return True





	

# Create your models here.
