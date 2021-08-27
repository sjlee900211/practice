from django.contrib import admin

# Register your models here.
from shareRes.models import Category, Restaurant


admin.site.register(Category)
admin.site.register(Restaurant)