from django.contrib import admin
from .models import custom_user,Sell,Cart
from django.contrib.auth.models import User

# Register your models here.

admin.site.register(custom_user)
# admin.site.register(Tag)
admin.site.register(Sell)
admin.site.register(Cart)
