from django.contrib import admin
#from django.contrib.admin.decorators import register
from .models import Enterprise, Store, Department, Transaction


# Register your models here.


admin.site.register(Enterprise)
admin.site.register(Store)
admin.site.register(Department)
admin.site.register(Transaction)
