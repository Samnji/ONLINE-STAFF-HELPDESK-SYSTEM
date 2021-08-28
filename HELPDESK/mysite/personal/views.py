from django.shortcuts import render, redirect
from account.models import Account
from personal.models import Task, Staff

def home_screen_view(request):
	context = {}
	accounts = Account.objects.all()
	context['accounts']= accounts
	return render(request, 'personal/Home Page.html')

def tasks(request):
	heading= 'TASKS ASSIGNED TODAY'
	queryset = Task.objects.all()
	context = {
		"heading":heading,
		"queryset":queryset,
	}
	return render(request, 'personal/Tasks.html', context)


def staff_members(request):
	heading= 'STAFF MEMBERS'
	queryset = Staff.objects.all()
	context = {
		"heading":heading,
		"queryset":queryset,
	}
	return render(request, 'personal/Staff Members.html',context)


def raise_issues(request):
	return render(request, 'personal/Raise Issues.html')


def assign_duties(request):
	return render(request, 'personal/Assign Duties.html')
# Create your views here.
