from django.contrib import admin

# Register your models here.
from .models import user

@admin.register(user) 
class useradmin(admin.ModelAdmin):
    list_display = ("id", "name","email","mobile","password" )

