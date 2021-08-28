from django.contrib import admin
from .models import Employee
from .models import Helpdesk_Support_team
from .models import Manager
from .models import Supervisor
from .models import Task
from .models import Staff

# Register your models here.
admin.site.register(Employee)
admin.site.register(Helpdesk_Support_team)
admin.site.register(Manager)
admin.site.register(Supervisor)
admin.site.register(Task)
admin.site.register(Staff)