from django.contrib import admin

# Register your models here.
from maindata.models import Category,Entertainer

admin.site.register(Category)
admin.site.register(Entertainer)