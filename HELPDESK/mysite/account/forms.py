from django import forms
from django.contrib.auth.forms import UserCreationForm
from account.models import Account


class RegistrationForm(UserCreationForm):
	staff_id=forms.CharField(max_length=10, help_text="Required. Add a valid staff_id")
	first_name=forms.CharField(max_length=15, help_text="Required. Add a valid first name")
	last_name=forms.CharField(max_length=15, help_text="Required. Add a valid last name")

	class Meta:
		model= Account
		fields= ("staff_id", "first_name", "last_name", "password1", "password2")

	



