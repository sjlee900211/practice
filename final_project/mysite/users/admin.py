from django.contrib import admin
from .models import User
# Register your models here.


# admin.site.register(User)

class UserAdmin(admin.ModelAdmin) :
    list_display = ('user_id', 'password')


admin.site.register(User, UserAdmin) #site에 등록