from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from account.forms import RegistrationForm
from account.models import Account
from django.contrib import messages, auth

def registration_view(request):
	context = {}
	if request.method == 'POST':
		staff_id = request.POST['staff_id']
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		password1 = request.POST['password1']
		password2 = request.POST['password2']

		if password1 == password2:
			if Account.objects.filter(staff_id=staff_id).exists():
				messages.info(request, "Staff Id Taken")
				return redirect('register')
			else:
				user = Account.objects.create_user(staff_id=staff_id, first_name=first_name, last_name=last_name, password=password1, )
				user.save();
				return redirect('login')
		else:
			messages.info(request, "Password Not Matching")
			return redirect('register')
		return redirect('login')

	else:
		return render(request, 'account/create.html', context)




def login(request):
	data_validation= 'Invalid staff_id or password'
	context = {
		"data_validation":data_validation
	}
	if request.method == 'POST':
		staff_id = request.POST['staff_id']
		password = request.POST['password']

		user = auth.authenticate(staff_id=staff_id,password=password)

		if user is not None:
			auth.login(request, user)
			return redirect('tasks')

		else:
			messages.info(request, " Invalid Password")
			return redirect('login')
	else:
		return render(request, 'account/login.html')



def logout(request):
	auth.logout(request)
	return redirect('')



