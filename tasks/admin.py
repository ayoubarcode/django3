from django.contrib import admin
from .models import  Task,Citizen,Category,Product

# Register your models here.

admin.site.register(Task)
admin.site.register(Citizen)
admin.site.register(Category)
admin.site.register(Product)